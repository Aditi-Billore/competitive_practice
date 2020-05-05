def main():
    arraylen = int(input("Enter array length"))
    mainArray = [0 for i in range(arraylen)]
    print(mainArray)
    queries = int(input("Enter number of queries"))

    dimArray = [[i for i in range(3)] for i in range(queries)]
    print(dimArray)

    for i in range(queries):
        line = input().split()
        dimArray[i][0] = int(line[0])
        dimArray[i][1] = int(line[1])
        dimArray[i][2] = int(line[2])
    print(dimArray)

    for i in range(queries):
        j = dimArray[i][0]
        while j<= dimArray[i][1]:
            mainArray[j-1] += dimArray[i][2]
            j += 1

    print(mainArray)

    mainArray.sort()
    print(mainArray[arraylen -1])


if __name__ == "__main__":
    main()
