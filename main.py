from memory import Memory


def main():
    am = Memory(16)
    am.randomize()
    print(am)
    print()
    diagonalised = am.diagonalise_copy()
    print("Diagonalized: ")
    print(diagonalised)
    print()
    res = am.search_in_range(am.memory,
                             [True, True, True, False, True, False, True, False, True, False, False, False, True,
                              True, True, False,
                              ],
                             [False, True, True, False, False, True, False, True, False, True, True, True, False,
                              True, False, True])
    first = [True, True, True, False, True, False, True, False, True, False, False, False, True,
             True, True, False,
             ]
    second = [False, True, True, False, False, True, False, True, False, True, True, True, False,
              True, False, True]
    print(f"Searching in interval {list(map(lambda x: int(x), first))} and {list(map(lambda x: int(x), second))}")
    for i in range(len(res)):
        print(" ".join(str(list(map(lambda x: int(x), res[i])))))
    print("logical 7-function")
    print(" ".join(str(list(map(lambda x: int(x), am.seventh_function(1, 2))))))
    print("logical 13-function")
    print(" ".join(str(list(map(lambda x: int(x), am.thirteenth_function(3, 4))))))
    print("logical 8-function")
    print(" ".join(str(list(map(lambda x: int(x), am.eighth_function(0, 1))))))
    print("addition")
    print(am.summarise_copy([True, True, True]))


if __name__ == "__main__":
    main()
