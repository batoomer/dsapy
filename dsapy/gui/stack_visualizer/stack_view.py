from ..config import tk, ttk


class StackView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        # Grid Configurations
        self.grid(row=0, column=0, sticky='news', padx=15, pady=15)
        self.grid_columnconfigure(1, weight=2)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=4)

        # ---- Operations Frame ----
        self.__operations_frame = ttk.LabelFrame(self, text='Operations')
        self.__operations_frame.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)

        self.__push_btn = ttk.Button(self.__operations_frame, text='Push')
        self.__push_btn.pack(fill='y', expand=True, pady=10)

        self.__pop_btn = ttk.Button(self.__operations_frame, text='Pop')
        self.__pop_btn.pack(fill='y', expand=True, pady=10)

        self.__del_btn = ttk.Button(self.__operations_frame, text='Delete')
        self.__del_btn.pack(fill='y', expand=True, pady=10)

        # ---- Status Frame ----
        self.__status_frame = ttk.LabelFrame(self, text='Stack Status')
        self.__status_frame.grid(row=1, column=0, sticky='nsew', padx=10, pady=10)
        self.__status_frame.grid_columnconfigure(0, weight=1)
        self.__status_frame.grid_columnconfigure(2, weight=1)
        self.__status_frame.grid_rowconfigure(0, weight=1)
        self.__status_frame.grid_rowconfigure(4, weight=1)

        self.__size_frame = StatusLabel(self.__status_frame, text='Size')
        self.__size_frame.grid(row=1, column=1, sticky='ew')

        self.__top_item_frame = StatusLabel(self.__status_frame, text='Top')
        self.__top_item_frame.grid(row=3, column=1, sticky='ew')

        # ---- Canvas Frame ----
        self.__canvas_frame = ttk.LabelFrame(self, text='Stack')
        self.__canvas_frame.grid(row=0, rowspan=2, column=1, sticky='news', padx=10, pady=10)

        self.__canvas = tk.Canvas(self.__canvas_frame)
        self.__canvas.pack(fill='both', side='left', expand=True, padx=15, pady=15)

        self.scroll_y = tk.Scrollbar(self.__canvas_frame, orient="vertical", command=self.__canvas.yview)
        self.scroll_y.pack(side='right', fill='y')
        self.__canvas.configure(yscrollcommand=self.scroll_y.set)

    def pop_btn(self):
        """
        Returns the Pop Button
        :return: Pop Button
        """
        return self.__pop_btn

    def push_btn(self):
        """
        Returns the Push Button

        :return: Push Button
        """
        return self.__push_btn

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

    def scroll_canvas(self):
        """
        Scrolls the canvas to the top.
        """
        self.__canvas.configure(scrollregion=self.__canvas.bbox("all"))
        if self.__canvas.yview()[0] != 0:
            self.__canvas.yview_moveto(0)

    def set_status(self, stats: dict):
        """
        Sets new values to the status labels

        :param stats: dictionary containing the statuses
        """
        self.__size_frame.set_value(stats['size'])
        self.__top_item_frame.set_value(stats['top'])

    def enable_operations(self):
        """
        Enables the operation buttons
        """
        self.__pop_btn.config(state='normal')
        self.__push_btn.config(state='normal')
        self.__del_btn.config(state='normal')

    def disable_operations(self):
        """
        Disables the operation buttons
        """
        self.__push_btn.config(state='disabled')
        self.__pop_btn.config(state='disabled')
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
