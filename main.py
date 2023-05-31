from memory import Memory


def main():
    am = Memory(16)
    am.randomize()
    print(am)
    print()
    diagonalised = am.diagonalise_copy()
    print(diagonalised)
    print()
    res = am.search_in_range(am.memory,
                             [True, True, True, False, True, False, True, False, True, False, False, False, True,
                              True, True, False,
                              ],
                             [False, True, True, False, False, True, False, True, False, True, True, True, False,
                              True, False, True])
    for element in res:
        print(element, "\n")
    print(am.seventh_function(1, 2))
    print(am.summarise_copy([True, True, True]), "cope")


if __name__ == "__main__":
    main()
