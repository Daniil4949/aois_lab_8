import random
from typing import List


class Flag:
    def __init__(self, greater, less):
        self.is_greater = greater
        self.is_lesser = less


class Memory:
    def __init__(self, size):
        self.size: int = size
        self.memory: List[bool] = [[False] * size for _ in range(size)]
        self.is_diagonalised: bool = False

    def add(self, first_value, second_value, attribute):
        self.memory[second_value][first_value] = attribute

    def add_word(self, word_address, attribute) -> None:
        if not self.is_diagonalised:
            if min(len(attribute), self.size) >= 0:
                for i in range(min(len(attribute), self.size)):
                    self.memory[word_address][i] = attribute[i]
        else:
            for i in range(word_address):
                self.memory[i][word_address] = attribute[len(attribute) - 1 - word_address + i]
            for i in range(word_address, self.size):
                self.memory[i][word_address] = attribute[i]

    def get(self, first_value, second_value) -> bool:
        return self.memory[second_value][first_value]

    def get_word(self, addr):
        if not self.is_diagonalised:
            return self.memory[addr]
        else:
            word = [self.memory[i][addr] for i in range(self.size)]
            word = word[-addr:] + word[:-addr]
            return word

    def get_column(self, address) -> List[bool]:
        result = [False] * self.size
        if not self.is_diagonalised:
            for i in range(self.size):
                result[i] = self.memory[i][address]
        else:
            for i in range(address):
                result[i] = self.memory[i][address - i][0]
            for i in range(address, self.size):
                result[i] = self.memory[i][-(i - address)][0]
            result = result[-address:] + result[:-address]
        return result

    def randomize(self) -> None:
        for _ in range(self.size * 3):
            for _ in range(self.size * 3):
                self.memory[random.randint(0, self.size - 1)][random.randint(0, self.size - 1)] ^= random.choice(
                    [True, False])

    def add_column(self, address, value):
        if not self.is_diagonalised:
            for i in range(self.size):
                self.memory[i][address] = value[i]
        else:
            for i in range(address):
                self.memory[i][self.size - 1 - address + i] = value[address + i]
            for i in range(address, self.size):
                self.memory[i][i - address] = value[i - address]

    def diagonalise_copy(self):
        result = Memory(self.size)
        for addr in range(self.size):
            result.add_column(addr, self.circular_shift(self.get_word(addr), addr))
        result.is_diagonalised = True
        return result

    @staticmethod
    def circular_shift(arr, k):
        return arr[k:] + arr[:k]

    def column_operation(self, first_column_index, second_column_index, function):
        result = [False] * self.size
        first_column = self.get_column(first_column_index)
        second_column = self.get_column(second_column_index)
        for i in range(self.size):
            result[i] = function(first_column[i], second_column[i])
        return result

    def second_function(self, first_column_index, second_column_index):
        return self.column_operation(first_column_index, second_column_index, lambda f, s: f and not s)

    def seventh_function(self, first_col_index, second_col_index):
        return self.column_operation(first_col_index, second_col_index, lambda f, s: f or s)

    def eighth_function(self, first_col_index, second_col_index):
        return self.column_operation(first_col_index, second_col_index, lambda f, s: not (f or s))

    def thirteenth_function(self, first_col_index, second_col_index):
        return self.column_operation(first_col_index, second_col_index, lambda f, s: not f or s)

    @staticmethod
    def compare_by_msb(first, second):
        for element in range(min(len(first), len(second)) - 1, -1, -1):
            if first[element] != second[element]:
                if first[element]:
                    return Flag(True, False)
                else:
                    return Flag(False, True)
        return Flag(False, False)

    def search_in_range(self, array, lower, upper):
        result: List = []
        for entry in array:
            if not self.compare_by_msb(entry, upper).is_greater and \
                    not self.compare_by_msb(entry, lower).is_lesser:
                result.append(entry)
        return result

    def summarise_copy(self, mask):
        result = Memory(self.size)

        for i in range(self.size):
            word = self.get_word(i)
            value = word[0:3]
            if value == mask:
                first_value = word[3:7]
                second_value = word[7:11]
                sum_result = self.binary_add(first_value, second_value)
                new_word = value + first_value + second_value + sum_result
                result.add_word(i, new_word)
            else:
                result.add_word(i, word)
        return result

    @staticmethod
    def binary_add(first_value, second_value) -> List[bool]:
        op_length = max(len(first_value), len(second_value))
        first_additional_value, second_additional_value, third_additional_value, result = False, False, False, False
        first_temp_add = [False] * (op_length + 1)
        second_temp_add = [False] * (op_length + 1)
        first_temp_add[:len(first_value)] = first_value
        second_temp_add[:len(second_value)] = second_value
        for i in range(op_length):
            first_additional_value = first_temp_add[i] ^ second_temp_add[i]
            second_additional_value = first_temp_add[i] and second_temp_add[i]
            third_additional_value = first_additional_value and result
            first_temp_add[i] = first_additional_value ^ result
            result = second_additional_value or third_additional_value
        first_temp_add[op_length] |= result
        return first_temp_add

    def __str__(self):
        result = str(self.memory)
        result = result.replace("], ", "\n")
        result = result.replace("False", "0")
        result = result.replace("True", "1")
        result = result.replace("[[", "")
        result = result.replace("[", "")
        result = result.replace("]]", "")
        result = result.replace("]", "")
        result = result.replace(",", "")
        return result
