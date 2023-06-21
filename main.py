import random

from solving import AssociativeProces

if __name__ == '__main__':

    object_ = AssociativeProces(16)

    for i in range(16):
        column = [random.randint(0, 1) for _ in range(16)]
        object_.add_item(i, column)

    print("Original Memory:")
    object_.show()

    object_.vice_versa()
    print("\nMemory with Diagonal Addressing:")
    object_.show()

    object_.to_normal()
    print("\nMemory with Original Addressing:")
    object_.show()
    object_.vice_versa()

    word = [random.randint(0, 1) for _ in range(16)]
    position = 2
    print(f'\nWriting word {word} on index {position}\nMemory:')
    object_.adding_item(position, word)
    object_.show()

    column = [random.randint(0, 1) for _ in range(16)]
    position = 2
    print(f'\nWriting column {column} on index {position}\nMemory:')
    object_.add_item(position, column)
    object_.show()

    print('\nLogical operations')
    print('x1*!x2', f'x1= 1st col = {object_.get_item(0)}', f'x2= 2nd col = {object_.get_item(1)}', sep='\n')
    print(f'ans = {object_.perform_logical_operation("f2", 0, 1)}')
    print()
    print('x1+x2 + x1*!x2', f'x1= 1st col = {object_.get_item(0)}', f'x2= 2nd col = {object_.get_item(1)}',
          sep='\n')
    print(f'ans = {object_.perform_logical_operation("f7", 0, 1)}')
    print()
    print('!(x1+x2)', f'x1= 1st col = {object_.get_item(0)}', f'x2= 2nd col = {object_.get_item(1)}',
          sep='\n')
    print(f'ans = {object_.perform_logical_operation("f8", 0, 1)}')
    print()
    print('!x1 + x2', f'x1= 1st col = {object_.get_item(0)}', f'x2= 2nd col = {object_.get_item(1)}', sep='\n')
    print(f'ans = {object_.perform_logical_operation("f13", 0, 1)}')
    print('\nArithmetic operations')

    print('V = 110')
    result, position = object_.operation("110")
    print(f'founded word index = {position}', sep='\n')
    print(f'ans = {result}')

    print(
        f"\nFind elements in range - [0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1] -  {int(''.join(list(map(lambda x: str(x), [0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1]))), 2)} and [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1] {int(''.join(list(map(lambda x: str(x), [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1]))), 2)}")
    res = object_.find_in_range(first_value=[0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1],
                                second_value=[0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1])
    for element in res:
        print(element, " ", int(''.join(list(map(lambda x: str(x), element))), 2))

    object_.show()
