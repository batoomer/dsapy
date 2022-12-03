from dsapy.gui.stack_visualizer.stack_model import StackModel
from dsapy.gui.stack_visualizer.stack_view import StackView


class StackController:
    def __init__(self, parent):
        # Model
        self.model = StackModel()
        # View
        self.view = StackView(parent)
        self.view.set_status(self.model.stats())
        self.__set_events()

    def __set_events(self):
        """
        Sets the commands and events of the view.
        """
        self.view.canvas().bind('<Configure>', lambda e: self.draw())
        self.view.push_btn().config(command=self.draw_push)
        self.view.pop_btn().config(command=self.draw_pop)
        self.view.del_btn().config(command=self.draw_delete)

    def draw(self):
        """
        Draws the stack to the canvas.
        """
        # Get the canvas from the view and the stack from the model
        canvas = self.view.canvas()
        stack = self.model.stack()

        # Clear the canvas
        canvas.delete('all')

        # Get the dimensions of the canvas
        max_width = canvas.winfo_width()
        max_height = canvas.winfo_height() - 25

        # Dimension of the cells
        height = width = 50

        # Gap between the cells
        gap = 10

        # x coordinates of the cells
        x0 = (max_width / 2) - (width / 2)
        x1 = (max_width / 2) + (width / 2)

        # y coordinate of the top cell
        max_y1 = max_height - height - gap

        if len(stack) == 0:
            # If the stack is empty draw a empty cell
            canvas.create_rectangle(x0, max_height - height, x1, max_height)
            canvas.create_text((x0 + x1) / 2, (2 * max_height - height) / 2, text=f'None', font=("", 16))

        else:
            # Loop through the stack
            for i in range(len(stack)):
                # Calculate the y coordinates
                y1 = max_height - i * (gap + height)
                y0 = y1 - height

                # Draw the cell
                item = canvas.create_rectangle(x0, y0, x1, y1)
                canvas.create_text((x0 + x1) / 2, (y0 + y1) / 2, text=f'{stack[i]}', font=("", 16))

                # Set a tag for the top cell
                if i == len(stack) - 1:
                    canvas.itemconfig(tagOrId=item, tag='top_element')

                # Update the top cell y coordinate
                max_y1 = y0 - gap

        # Draw the top pointer
        canvas.create_line(max_width / 2, max_y1, max_width / 2, max_y1 - 50, arrow='first')
        canvas.create_text(max_width / 2, max_y1 - 75, text=f'TOP', font=("", 16), tag='top_pointer')

        # Scroll to the top
        self.view.scroll_canvas()

    def draw_push(self):
        """
        Pushes an element onto the stack, redraws the stack and updates the stack status.
        """
        self.view.disable_operations()
        self.model.push()
        self.draw()
        self.highlight_top('green')
        self.view.set_status(self.model.stats())
        self.view.enable_operations()

    def draw_pop(self):
        """
        Pops an element from the stack, redraws the stack and updates the stack status.
        """
        self.view.disable_operations()
        self.model.pop()
        self.highlight_top('red')
        self.draw()
        self.view.set_status(self.model.stats())
        self.view.enable_operations()

    def draw_delete(self):
        """
        Deletes the stack and redraws it.
        """
        self.model.delete()
        self.draw()

    def highlight_top(self, color):
        """
        Highlights the top element of the stack, by changing its color.

        :param color: color to change to.
        """
        canvas = self.view.canvas()
        canvas.itemconfig('top_element', fill=color)
        canvas.update_idletasks()
        canvas.after(250, canvas.itemconfig('top_element', fill=canvas['background']))
