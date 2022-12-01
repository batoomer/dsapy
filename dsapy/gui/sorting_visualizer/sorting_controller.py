from .sorting_model import SortingModel
from .sorting_view import SortingView, DELAY_CONFIG, ALGORITHM_CONFIG


class SortingController:

    def __init__(self, parent):
        # The Model and the View of the visualizer
        self.model = SortingModel()
        self.view = SortingView(parent)

        # Flag to Control (start/stop) the Animation
        self.__running = False
        # Variable to control the speed of the animation
        self.__delay = DELAY_CONFIG['init_val']
        # Variable to select the algorithm
        self.__algorithm = ALGORITHM_CONFIG['algorithms'][0]

        # Events and commands of the view
        self.__add_events()

    def __add_events(self):
        """
        Adds commands and binds events to the widgets of the view.
        """
        self.view.shuffle_btn().config(command=self.shuffle)
        self.view.start_btn().config(command=self.start_sort)
        self.view.stop_btn().config(command=self.stop_sort)
        self.view.size_scale()[0].config(command=self.set_size)
        self.view.delay_scale()[0].config(command=self.set_delay)
        self.view.algorithm_combobox().bind('<<ComboboxSelected>>', self.set_algorithm)

        self.view.canvas().bind('<Configure>', lambda e: self.draw(self.model.data()))

    # ---- CANVAS FUNCTIONS -----
    def draw(self, data: list):
        """
        Draws the data on the canvas. Each item in the data is represented by a vertical bar.
        The value of the item is correlated with the height of the bar.
        The index of the item is correlated with the position of the bar on the x-axis
        :param data:
        """
        # Get the canvas widget of the view
        canvas = self.view.canvas()
        # Reset the canvas
        canvas.delete('all')

        # Get the dimensions of the canvas
        max_width = canvas.winfo_width()
        max_height = canvas.winfo_height()

        # Normalize the data, such that the maximum item has a value of 1.
        data = [item / max(data) for item in data]

        # The number of bars is: SIZE
        # The number of gaps is: SIZE + 1
        # The max_width must equal to: max_width = SIZE*bar_width + (SIZE-1)*gap_width
        # We also choose: bar_width = 10*gap_width
        # Solving the equations above we get,
        # gap_width = max_width/(11*SIZE -1)
        # bar_width = 10*max_width/(11*SIZE -1)
        gap = max_width / (11 * len(data) - 1)
        bar_width = 10 * gap

        for i, x in enumerate(data):
            # Calculate the x coordinates
            x0 = i * (bar_width + gap)
            x1 = i * (bar_width + gap) + bar_width

            # Calculate the y coordinates
            y0 = max_height - x * max_height
            y1 = max_height

            # Draw the bar and tag it with f+index, e.g. for index 11 -> tag=t11
            canvas.create_rectangle(x0, y0, x1, y1, fill='blue', outline='', tag=f't{i}')

        canvas.update_idletasks()

    def refill_rect(self, tag: int, color: str):
        """
        Changes the color of a bar.

        :param tag: index of the bar in the model data.
        :param color: color to paint the bar
        """
        # Get the canvas of the view
        canvas = self.view.canvas()
        # Change the color of the target bar
        canvas.itemconfig(f't{tag}', fill=color)
        canvas.update_idletasks()

    def swap_rect(self, tag_i, tag_j):
        """
        Swaps the positions of two bars
        :param tag_i: index of the first bar in the model data.
        :param tag_j: index of the second bar in the model data.
        """

        # Get the canvas of the view
        canvas = self.view.canvas()

        # Get the coordinates of the two bars
        x0_i, y0_i, x1_i, y1_i = canvas.coords(f't{tag_i}')
        x0_j, y0_j, x1_j, y1_j = canvas.coords(f't{tag_j}')

        # Swap their heights by swapping their y coordinates.
        canvas.coords(f't{tag_i}', x0_i, y0_j, x1_i, y1_j)
        canvas.coords(f't{tag_j}', x0_j, y0_i, x1_j, y1_i)
        canvas.update_idletasks()

    # ---- EVENTS AND COMMANDS -----
    def shuffle(self):
        """
        Shuffles the data of the model and redraws it on the canvas of the view
        """
        # Shuffle data
        self.model.shuffle()
        # Redraw data
        self.draw(self.model.data())

    def set_size(self, val):
        """
        Gets the input of the size scale from the view, and then it
        resizes the data of the model and redraws it on the canvas
        of the view.
        """
        _, size_label = self.view.size_scale()
        # Get new size
        new_size = int(round(float(val)))
        # Set new size
        self.model.set_size(new_size)
        # Redraw new data
        self.draw(self.model.data())
        # Display new value
        size_label.config(text=new_size)

    def set_delay(self, val):
        """
        Gets the input of the delay scale form the view, and sets
        the text of the delay label to the new value.

        :param val: Value of the delay scale
        """
        _, delay_label = self.view.delay_scale()
        # Get new delay
        new_delay = int(round(float(val)))
        # Set new delay
        self.__delay = new_delay
        # Display new value
        delay_label.config(text=self.__delay)

    def set_algorithm(self, event):
        """
        Gets the algorithm selection from the view and sets its value to the controller.
        :param event:
        """
        self.__algorithm = str(event.widget.get())

    def stop_sort(self):
        """
        Stops the execution of the animation by setting the running flag to false.
        """
        if self.__running:
            self.__running = False
            self.view.enable_controls()

    def start_sort(self):
        """
        Starts the sorting animation and disables the controls.
        """
        # Set the running flag to true
        self.__running = True
        if self.__running:
            # Disable the controls of the view
            self.view.disable_controls()

            # Generate the sorting animation and the metadata
            self.model.sort(self.__algorithm)
            metadata = self.model.get_metadata()

            # Display the metadata and animate the algorithm
            self.view.set_metadata(metadata)
            self.__animate()

    def __animate(self):
        """
        Animates the sorting algorithm. This function loops
        its self.
        """
        # If the running flag is true
        if self.__running:
            # Get the swapped indices
            indices = self.model.get_animation()

            # If indices the algorithm has not finished
            if indices:
                # Paint the swapped items with red
                self.refill_rect(indices[0], 'red')
                self.refill_rect(indices[1], 'red')
                self.view.after(10 * self.__delay)
                # Swap the bars on the view and the values at the model
                self.swap_rect(indices[0], indices[1])
                self.model.swap(indices[0], indices[1])

                # Paint the swapped items with red
                self.refill_rect(indices[0], 'blue')
                self.refill_rect(indices[1], 'blue')

                # Loop self
                self.view.after(1, self.__animate)
            else:
                # if indices is non, the sorting has ended
                # Set the running flag to false
                self.__running = False
                self.view.enable_controls()
