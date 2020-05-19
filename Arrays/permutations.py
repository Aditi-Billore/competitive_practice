from itertools import permutations

def performPermutation(list1):
    return list(permutations(list1, len(list1)))


def main():
    list1 = [1,2,3]

    perm = performPermutation(list1)
    print(perm)

if __name__ == "__main__":
    main()
