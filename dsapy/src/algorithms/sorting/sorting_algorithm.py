from abc import ABC, abstractmethod
from time import process_time


class SortingAlgorithm(ABC):
    def __init__(self):
        self.__stop_time = None
        self.__start_time = None
        self.__metadata = {}
        self.__animations = {}

    def _reset_metadata_animations(self):
        self.__metadata = {
            'swap_count': 0,
            'comparison_count': 0,
            'iteration_count': 0,
            'runtime': 0.0,
        }

        self.__animations = {
            'swap': [],
        }

    def _add_swap(self, i, j):
        self.__metadata['swap_count'] += 1
        self.__animations['swap'].append([i, j])

    def _add_comparison(self):
        self.__metadata['comparison_count'] += 1

    def _add_iteration(self):
        self.__metadata['iteration_count'] += 1

    def _add_runtime(self):
        self.__metadata['runtime'] = round(1000 * (self.__stop_time - self.__start_time), 2)

    def _start_runtime(self):
        self.__start_time = process_time()

    def _stop_runtime(self):
        self.__stop_time = process_time()

    def metadata(self):
        return self.__metadata

    def animation(self):
        return self.__animations

    @abstractmethod
    def sort(self, data: list[int | float | str]) -> list[int | float | str]:
        pass
