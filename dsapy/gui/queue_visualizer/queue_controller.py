from dsapy.gui.queue_visualizer.queue_model import QueueModel
from dsapy.gui.queue_visualizer.queue_view import QueueView


class QueueController:
    def __init__(self, parent):
        # Model
        self.model = QueueModel()

        # View
        self.view = QueueView(parent)
        self.view.set_status(self.model.stats())
        self.__set_events()

    def __set_events(self):
        """
        Sets the commands and events of the view.
        """
        self.view.canvas().bind('<Configure>', lambda e: self.draw())
        self.view.enqueue_btn().config(command=self.draw_enqueue)
        self.view.dequeue_btn().config(command=self.draw_dequeue)
        self.view.del_btn().config(command=self.draw_delete)

    def draw(self):
        # Get the queue from the model
        queue = self.model.queue()
        # Get the canvas from the view and clear it
        canvas = self.view.canvas()
        canvas.delete('all')

        # Get the max height of the canvas
        max_height = canvas.winfo_height()

        # Cell height, width, and gap between cells
        c_height = c_width = 50
        gap = 20

        # y coordinates of the cells
        y0 = (max_height / 2) - c_height / 2
        y1 = (max_height / 2) + c_height / 2

        # Draw the Front pointer
        canvas.create_text(50, (y0 + y1) / 2, text=f'FRONT', font=("", 16))
        canvas.create_line(80, (y0 + y1) / 2, 140, (y0 + y1) / 2, arrow='first')

        # Starting x coordinates of the cells
        start_x0 = 150
        start_x1 = start_x0 + 50

        # Last cell x coordinate
        max_x1 = start_x1

        if len(queue) == 0:
            # if queue is empty draw an empty cell
            canvas.create_rectangle(start_x0, y0, start_x1, y1)
            canvas.create_text((start_x1+start_x0)/2, (y1+y0)/2, text='None')
        else:
            for i in range(len(queue)):
                # x coordinates of the cell
                x0 = start_x0 + i * (gap + c_width)
                x1 = x0 + c_width

                # draw the cell
                item = canvas.create_rectangle(x0, y0, x1, y1)
                canvas.create_text((x0 + x1) / 2, (y0 + y1) / 2, text=f'{queue[i]}')

                # Front cell
                if i == 0:
                    canvas.itemconfig(tagOrId=item, tag='front_element')

                # Rear cell
                if i == len(queue) - 1:
                    canvas.itemconfig(tagOrId=item, tag='rear_element')

                # If only 1 cell exists it is both the front and rear cell
                if len(queue) == 1:
                    canvas.itemconfig(tagOrId=item, tags=('front_element', 'rear_element'))

                # update the last cell x coordinate
                max_x1 = x1

        # Draw the Rear pointer
        canvas.create_line(max_x1 + 10, (y0 + y1) / 2, max_x1 + 10 + 60, (y0 + y1) / 2, arrow='first')
        canvas.create_text(max_x1 + 10 + 60 + 25, (y0 + y1) / 2, text=f'REAR', font=("", 16))

    def draw_enqueue(self):
        """
        Enqueues and item from the queue, and redraws the queue.
        :return:
        """
        self.view.disable_operations()
        self.model.enqueue()
        self.view.set_status(self.model.stats())
        self.draw()
        self.highlight_rear()
        self.view.enable_operations()

    def draw_dequeue(self):
        """
        Dequeues an item from the queue, and redraws the queue.
        :return:
        """
        self.view.disable_operations()
        self.model.dequeue()
        self.view.set_status(self.model.stats())
        self.highlight_front()
        self.draw()
        self.view.enable_operations()

    def draw_delete(self):
        """
        Deletes the queue and redraws it
        """
        self.model.delete()
        self.draw()
        self.view.scroll_canvas('dequeue')

    def highlight_front(self):
        """
        Highlights the front element of the queue, by changing its color and scrolling to it.
        """
        canvas = self.view.canvas()
        self.view.scroll_canvas('dequeue')
        canvas.itemconfig('front_element', fill='red')
        canvas.update_idletasks()
        canvas.after(250, canvas.itemconfig('front_element', fill=canvas['background']))

    def highlight_rear(self):
        """
        Highlights the front element of the queue, by changing its color and scrolling to it.
        """
        canvas = self.view.canvas()
        self.view.scroll_canvas('enqueue')
        canvas.itemconfig('rear_element', fill='green')
        canvas.update_idletasks()
        canvas.after(250, canvas.itemconfig('rear_element', fill=canvas['background']))
