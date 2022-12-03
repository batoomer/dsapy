from config import *
from dsapy.gui.sorting_visualizer.sorting_controller import SortingController
from dsapy.gui.stack_visualizer.stack_controller import StackController


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Set the windows settings
        self.attributes('-fullscreen', True)
        self.minsize(int(3 * self.winfo_screenwidth() / 4), int(3 * self.winfo_screenheight() / 4))
        self.title('Algorithms and Data Structures')
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.controller = StackController(self)


if __name__ == '__main__':
    app = App()
    app.mainloop()
