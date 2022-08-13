import random
import threading


class SumThread(threading.Thread):
    def __init__(self, lo, hi, list_nums):
        super().__init__()
        self.lo = lo
        self.hi = hi
        self.list_nums = list_nums
        self.sum = 0

    def run(self):
        self.find_max()

    def find_max(self):
        i = self.lo
        while i < self.hi:
            for idx_i in range(self.list_nums[i]):
                for idx_j in range(self.list_nums[i]):
                    if self.list_nums[idx_i] > self.list_nums[idx_j]:
                        return self.list_nums[idx_i]
                    else:
                        return self.list_nums[idx_j]


    def print_list(self):
        str_list = ''
        i = self.lo
        while i < self.hi:
            str_list += str(self.list_nums[i]) + "; "
            i += 1
            return str_list


def threadinng(list_numbers, n_threads):
    tong = 0
    so_pt = len(list_numbers)
    list_threads = []
    i = 0
    while i < n_threads:
        lo = int(i * so_pt / n_threads)
        hi = int((i + 1 * so_pt) / n_threads)
        thread = SumThread(lo, hi, list_numbers)
        list_threads.append(thread)
        list_threads[i].start()
        i += 1
    j = 0
    while j < n_threads:
        list_threads[j].join()
        tong += list_threads[j].find_max()
        print("Thread", j + 1, ":", list_threads[j].print_list())
        j += 1
        return tong


if __name__ == "__main__":
    list_numbers = []
    n = int(input("Nhap so phan tu \t"))
    i = 0
    while i < n:
        list_numbers.append(random.randrange(10))
        i += 1
    print("List: ", list_numbers)
    n_threads = int(input("Nhap so threads: \t"))
    max = threadinng(list_numbers, n_threads)
    print("Max number=", max)
