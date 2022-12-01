from ..config import tk, ttk
from .sorting_config import *


class SortingView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.grid(row=0, column=0, sticky='news', padx=15, pady=15)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=4)
        self.grid_columnconfigure(1, weight=1)

        # ---- Controls ----
        self.__controls = SortingViewControls(self)
        self.__controls.grid(row=0, columnspan=2, sticky='we', pady=15)

        # ---- Canvas Frame ----
        self.__canvas_frame = ttk.LabelFrame(self, text='Visualization')
        self.__canvas_frame.grid(row=1, column=0, sticky='news')
        self.__canvas = tk.Canvas(self.__canvas_frame)
        self.__canvas.pack(fill='both', expand=True, padx=15, pady=15)

        # ---- Metadata Frame ----
        self.__metadata_frame = ttk.LabelFrame(self, text='Metadata')
        self.__metadata_frame.grid(row=1, column=1, sticky='news', padx=15)

        self.__iterations_label = ttk.Label(self.__metadata_frame, text=f'Iterations: {0}')
        self.__iterations_label.pack(fill='x', expand=True, padx=10)

        self.__comparisons_label = ttk.Label(self.__metadata_frame, text=f'Comparisons: {0}')
        self.__comparisons_label.pack(fill='x', expand=True, padx=10)

        self.__swaps_label = ttk.Label(self.__metadata_frame, text=f'Swaps: {0}')
        self.__swaps_label.pack(fill='x', expand=True, padx=10)

        self.__runtime_label = ttk.Label(self.__metadata_frame, text=f'CPU Runtime: {0}ms')
        self.__runtime_label.pack(fill='x', expand=True, padx=10)

    def canvas(self):
        """
        Returns the canvas.

        :return: Canvas
        """
        return self.__canvas

    def shuffle_btn(self) -> ttk.Button:
        """
        Returns the Shuffle Button

        :return: Shuffle Button
        """
        return self.__controls.shuffle_btn()

    def size_scale(self) -> tuple[ttk.Scale, ttk.Label]:
        """
        Returns the size scale and the size scale value label.

        :return: Tuple containing the size scale and the size scale value label.
        """
        return self.__controls.size_scale()

    def delay_scale(self) -> tuple[ttk.Scale, ttk.Label]:
        """
        Returns the delay scale and the delay scale value label.

        :return: Tuple containing the delay scale and the delay scale value label.
        """
        return self.__controls.delay_scale()

    def algorithm_combobox(self) -> ttk.Combobox:
        """
        Returns the algorithm combobox.

        :return: Algorithm Combobox
        """
        return self.__controls.algorithm_combobox()

    def start_btn(self) -> ttk.Button:
        """
        Returns the Start button

        :return: Start Button
        """
        return self.__controls.start_btn()

    def stop_btn(self):
        """
        Return the Stop button

        :return: Stop Button
        """
        return self.__controls.stop_btn()

    def disable_controls(self):
        """
        Disables the controls, except the stop button which gets enabled
        """
        return self.__controls.disable_controls()

    def enable_controls(self):
        """
        Disables the controls, except the stop button which gets disabled
        """
        return self.__controls.enable_controls()

    def set_metadata(self, metadata):
        """
        Sets the metadata labels with the corresponding values.

        :param metadata: Dictionary containing the metadata
        """
        self.__iterations_label.config(text=f"Iterations: {metadata['iteration_count']}")
        self.__comparisons_label.config(text=f"Comparisons: {metadata['comparison_count']}")
        self.__swaps_label.config(text=f"Swaps: {metadata['swap_count']}")
        self.__runtime_label.config(text=f"CPU runtime: {metadata['runtime']}ms")


class SortingViewControls(ttk.LabelFrame):
    # Horizontal Padding
    __PAD_X = 10

    def __init__(self, parent):
        super().__init__(parent, text='Controls')
        # ---- CONFIG GRID ----
        self.grid_rowconfigure(1, weight=1)
        # column 0 and 7 have weights, so that everything between gets centered horizontally
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(7, weight=1)

        # ---- SHUFFLE BUTTON ----
        self.__shuffle_btn = ttk.Button(self, text='Shuffle')
        self.__shuffle_btn.grid(row=1, column=1, padx=self.__PAD_X, sticky='ns')

        # ---- DATA SIZE SCALE ----
        self.__data_size = tk.IntVar()
        self.__data_size.set(SIZE_CONFIG['init_val'])
        self.__size_scale_label = ttk.Label(self, text='Size')
        self.__size_scale_label.grid(row=0, column=2)
        self.__size_scale = ttk.Scale(self, from_=SIZE_CONFIG['from'], to=SIZE_CONFIG['to'], variable=self.__data_size)
        self.__size_scale.grid(row=1, column=2, padx=self.__PAD_X, sticky='ns')
        self.__size_scale_value_label = ttk.Label(self, text=SIZE_CONFIG['init_val'])
        self.__size_scale_value_label.grid(row=2, column=2)

        # ---- ALGORITHM COMBOBOX ----
        self.__algorithm = tk.StringVar()
        self.__algorithm.set(ALGORITHM_CONFIG['algorithms'][0])
        self.__algorithm_combobox = ttk.Combobox(self, values=ALGORITHM_CONFIG['algorithms'], state='readonly')
        self.__algorithm_combobox.current(0)
        self.__algorithm_combobox.grid(row=1, column=3, padx=self.__PAD_X, sticky='ns')

        # ---- DELAY SCALE ----
        self.__delay = tk.IntVar()
        self.__delay.set(DELAY_CONFIG['init_val'])
        self.__delay_scale_label = ttk.Label(self, text='Delay')
        self.__delay_scale_label.grid(row=0, column=4)
        self.__delay_scale = ttk.Scale(self, from_=DELAY_CONFIG['from'], to=DELAY_CONFIG['to'], variable=self.__delay)
        self.__delay_scale.grid(row=1, column=4, padx=self.__PAD_X, sticky='ns')
        self.__delay_scale_value_label = ttk.Label(self, text=DELAY_CONFIG['init_val'])
        self.__delay_scale_value_label.grid(row=2, column=4)

        # ---- START BUTTON ----
        self.__start_btn = ttk.Button(self, text='Start')
        self.__start_btn.grid(row=1, column=5, padx=self.__PAD_X, sticky='ns')

        # ---- STOP BUTTON ----
        self.__stop_btn = ttk.Button(self, text='Stop')
        self.__stop_btn.grid(row=1, column=6, padx=self.__PAD_X, sticky='ns')

    def disable_controls(self):
        """
        Disables all control widgets, except the stop button which gets enabled
        """
        self.__stop_btn.config(state='enabled')
        self.__start_btn.config(state='disabled')
        self.__size_scale.config(state='disabled')
        self.__shuffle_btn.config(state='disabled')
        self.__delay_scale.config(state='disabled')
        self.__algorithm_combobox.config(state='disabled')

    def enable_controls(self):
        """
        Enables all control widgets, except the stop button which gets disabled
        """
        self.__stop_btn.config(state='disabled')
        self.__start_btn.config(state='normal')
        self.__size_scale.config(state='normal')
        self.__shuffle_btn.config(state='normal')
        self.__delay_scale.config(state='normal')
        self.__algorithm_combobox.config(state='readonly')

    def shuffle_btn(self) -> ttk.Button:
        """
        Returns the shuffle button
        :return: Shuffle Button
        """
        return self.__shuffle_btn

    def size_scale(self) -> tuple[ttk.Scale, ttk.Label]:
        """
        Returns the size scale and the size scale value label

        :return: Tuple containing the size scale and the size scale value label.
        """
        return self.__size_scale, self.__size_scale_value_label

    def delay_scale(self) -> tuple[ttk.Scale, ttk.Label]:
        """
        Returns the delay scale and the delay scale value label

        :return: Tuple containing the delay scale and the delay scale value label.
        """
        return self.__delay_scale, self.__delay_scale_value_label

    def start_btn(self) -> ttk.Button:
        """
        Returns the start button

        :return: Start Button
        """
        return self.__start_btn

    def stop_btn(self) -> ttk.Button:
        """
        Returns the stop button.

        :return: Stop Button
        """
        return self.__stop_btn

    def algorithm_combobox(self) -> ttk.Combobox:
        """
        Returns the Algorithm Combobox

        :return: algorithm combobox
        """
        return self.__algorithm_combobox
