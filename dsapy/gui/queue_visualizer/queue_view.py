from ..config import tk, ttk


class QueueView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Grid Configurations
        self.grid(row=0, column=0, sticky='news', padx=15, pady=15)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=4)

        # ---- Operations Frame ----
        self.__operations_frame = ttk.LabelFrame(self, text='Operations')
        self.__operations_frame.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)

        self.__enqueue_btn = ttk.Button(self.__operations_frame, text='Enqueue')
        self.__enqueue_btn.pack(fill='y', expand=True, pady=10)

        self.__dequeue_btn = ttk.Button(self.__operations_frame, text='Dequeue')
        self.__dequeue_btn.pack(fill='y', expand=True, pady=10)

        self.__del_btn = ttk.Button(self.__operations_frame, text='Delete')
        self.__del_btn.pack(fill='y', expand=True, pady=10)

        # ---- Status Frame ----
        self.__status_frame = ttk.LabelFrame(self, text='Stack Status')
        self.__status_frame.grid(row=0, column=1, sticky='nsew', padx=10, pady=10)
        self.__status_frame.grid_columnconfigure(0, weight=1)
        self.__status_frame.grid_columnconfigure(2, weight=1)
        self.__status_frame.grid_rowconfigure(0, weight=1)
        self.__status_frame.grid_rowconfigure(4, weight=1)

        self.__size_frame = StatusLabel(self.__status_frame, text='Size')
        self.__size_frame.grid(row=1, column=1, sticky='ew')

        self.__front_item_frame = StatusLabel(self.__status_frame, text='Front')
        self.__front_item_frame.grid(row=3, column=1, sticky='ew')

        # ---- Canvas Frame ----
        self.__canvas_frame = ttk.LabelFrame(self, text='Queue')
        self.__canvas_frame.grid(row=1, column=0, columnspan=2, sticky='news', padx=10, pady=10)

        self.__canvas = tk.Canvas(self.__canvas_frame)
        self.__canvas.pack(fill='both', side='top', expand=True, padx=15, pady=15)

        self.__scroll_x = tk.Scrollbar(self.__canvas_frame, orient="horizontal", command=self.__canvas.xview)
        self.__scroll_x.pack(side='bottom', fill='x')
        self.__canvas.configure(xscrollcommand=self.__scroll_x.set)

    def enqueue_btn(self):
        """
        Returns the Enqueue Button
        :return: Enqueue Button
        """
        return self.__enqueue_btn

    def dequeue_btn(self):
        """
        Returns the Dequeue Button

        :return: Dequeue Button
        """
        return self.__dequeue_btn

    def del_btn(self):
        """
        Returns the delete button.

        :return: Delete Button
        """
        return self.__del_btn

    def canvas(self):
        """
        Returns the canvas

        :return: canvas
        """
        return self.__canvas

    def scroll_canvas(self, type):
        """
        Scrolls the canvas to the top.
        """
        self.__canvas.configure(scrollregion=self.__canvas.bbox("all"))
        if type == 'enqueue':
            self.__canvas.xview_moveto(1)
        else:
            self.__canvas.xview_moveto(0)

    def set_status(self, stats: dict):
        """
        Sets new values to the status labels

        :param stats: dictionary containing the statuses
        """
        self.__size_frame.set_value(stats['size'])
        self.__front_item_frame.set_value(stats['front'])

    def enable_operations(self):
        """
        Enables the operation buttons
        """
        self.__enqueue_btn.config(state='normal')
        self.__dequeue_btn.config(state='normal')
        self.__del_btn.config(state='normal')

    def disable_operations(self):
        """
        Disables the operation buttons
        """
        self.__enqueue_btn.config(state='disabled')
        self.__dequeue_btn.config(state='disabled')
        self.__del_btn.config(state='disabled')


class StatusLabel(ttk.Frame):
    def __init__(self, parent, text='', value=''):
        super().__init__(parent)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(4, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)

        self.__label = ttk.Label(self, text=f'{text}:')
        self.__label.grid(row=1, column=1, columnspan=2, padx=5, pady=25)
        self.__value_label = ttk.Label(self, text=value)
        self.__value_label.grid(row=1, column=3, padx=5, pady=25)

    def set_value(self, val):
        """
        Sets the value of the label value.

        :param val: Value to set
        """
        self.__value_label.config(text=val)
