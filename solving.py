

class AssociativeProces:
    def __init__(self, order):
        self.bits_data = [[0] * order for _ in range(order)]
        self.order = order
        self.ACTIONS = {'f2': self.second_function,
                        'f7': self.seventh_function,
                        'f8': self.eight_function,
                        'f13': self.thirteenth_function
                        }

    def vice_versa(self):
        result = []
        for i in range(self.order):
            shifted_word = self.changing(self.bits_data[i], i)
            result.append(shifted_word)
        result_transposed = []
        for column in zip(*result):
            result_transposed.append(list(column))
        self.bits_data = result_transposed

    @staticmethod
    def changing(item: list, element: int):
        fact = False
        if element < 0:
            element = -element
            fact = True
        item = list(item)
        for _ in range(element):
            if not fact:
                item.insert(0, item.pop())
            else:
                item.append(item.pop(0))

        return list(item)

    def to_normal(self):
        result_transposed = []
        for column in zip(*self.bits_data):
            result_transposed.append(list(column))
        self.bits_data = result_transposed
        result = []
        for i in range(self.order):
            changed_element = self.changing(self.bits_data[i], -i)
            result.append(changed_element)
        self.bits_data = result

    def get_item(self, position: int):
        column_data = []
        for i in range(self.order):
            index = (i + position) % self.order
            column_data.append(self.bits_data[i][index])
        return column_data

    def add_item(self, position: int, items: list):
        self.bits_data = list(map(list, self.bits_data))
        for i in range(self.order):
            word = self.getting_item(i)
            word[position] = items[i]
            self.adding_item(i, word)

    def getting_item(self, position: int):
        return self.changing(
            self.bits_data[position],
            -position)

    def adding_item(self, position: int, data: list):
        self.bits_data = list(map(list, self.bits_data))
        for i in range(self.order): self.bits_data[i][position] = self.changing(data, position)[i]

    @staticmethod
    def second_function(digit1: int, digit2: int):
        return int(digit1 and (not digit2))

    @staticmethod
    def seventh_function(digit1: int, digit2: int):
        return int(digit1 or digit2)

    @staticmethod
    def eight_function(digit1: int, digit2: int):
        return int(not int((digit1 and digit2)))

    @staticmethod
    def thirteenth_function(digit1: int, digit2: int):
        return int((not digit1) or digit2)

    def perform_logical_operation(self, operation: str, first_value, second_value):
        first_position = self.get_item(first_value), self.get_item(second_value)
        second_position = self.get_item(second_value)
        return ''.join(
            list(
                map(lambda x: str(self.ACTIONS[operation](*x)),
                    list(zip(first_position, second_position)
                         ))))

    def operation(self, v_value: str):
        v_value = list(map(int, v_value))
        value, suitable_items = self.finding_item(v_value)
        first = suitable_items[3:7]
        second = suitable_items[7:11]
        result = suitable_items[:11] + self.arithmetic_operation(first, second)
        return " ".join(list(map(str, result))), value

    def finding_item(self, v_value):
        value = 0
        suitable_items = []
        for i in range(self.order):
            word = self.getting_item(i)
            print(word)
            if word[:3] == v_value:
                value = i
                suitable_items = word
        return value, suitable_items

    def arithmetic_operation(self, first_item, second_item):
        first_value, second_value = [int(x) for x in first_item], [int(x) for x in second_item]
        result, additional_bit = self.additional_action(first_value, second_value)
        result = str(additional_bit) + result
        return list(result)

    @staticmethod
    def additional_action(first_value, second_value):
        result, additional_bit = '', 0
        while len(first_value) and len(second_value):
            first_bit, second_bit = first_value.pop(), second_value.pop()
            second_bit = second_value.pop()
            res = int(first_bit ^ second_bit ^ additional_bit)
            result = str(res) + result
            additional_bit = int((first_bit and second_bit) or (first_bit ^ second_bit) and additional_bit)
        return result, additional_bit

    def find_in_range(self, first_value=None, second_value=None):
        self.bits_data.sort()
        memory_data = self.bits_data
        result_data: list = []
        for item in memory_data:
            if self.compare(item, first_value) == 1 and self.compare(item, second_value) == -1: result_data.append(item)
        return result_data

    def comparing_bits(self, first_value: str, second_value: str):
        current_g = 0
        current_l = 0
        for ind, word in enumerate(self.bits_data):
            digit_1, digit_2 = list(map(lambda x: bool(int(x)), [first_value[ind], second_value[ind]]))
            next_g = current_g or (not digit_2 and digit_1 and not current_l)
            next_l = current_l or (digit_2 and not digit_1 and not current_g)
            current_g = next_g
            current_l = next_l
        return bool(current_g), bool(current_l)

    def compare(self, first_value: str, second_value: str):
        res = self.comparing_bits(first_value, second_value)
        if res == (True, False): return 1
        elif res == (False, True): return -1
        elif res == (False, False): return 0

    def show(self):
        for row in self.bits_data:
            print(' '.join(map(str, row)))
