from memory import Memory


def main():
    am = Memory(16)
    am.randomize()
    print(am)
    print()
    diagonalised = am.diagonalise_copy()
    print(diagonalised)
    print()
    print(am.search_in_range(am.memory,
                             [True, True, True, False, True, False, True, False, True, False, False, False, True,
                              True, True, False,
                              ],
                             [False, True, True, False, False, True, False, True, False, True, True, True, False,
                              True, False, True]))
    print(am.seventh_function(1, 2))


if __name__ == "__main__":
    main()
