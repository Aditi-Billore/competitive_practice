#check connected components in a graph

import fileinput
import sys

class datastruct:

    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.listing =  [i for i in range(maxsize)]

    def find(self, num):
        return num in self.listing

    def union(self, num1, num2):

        check =  self.listing[num1]

        while check in self.listing:
            indexI = self.listing.index(check)
            self.listing[indexI] = self.listing[num2]

        return

    def isConnected(self, num1, num2):
        return self.listing[num1] == self.listing[num2]

    def connectedComponets(self):
        list_set = set(self.listing)
        unique_list = list(list_set)
        return len(unique_list)

    def __str__(self):
        return "String is looking like "

    def __repr__(self):
        return "List is : {}".format(self.listing)


def main():
    isStdin = True

    num = int(input("Give max size of list: "))
    graph = datastruct(num)

    for line in sys.stdin:
        if 'Exit' == line.rstrip():
            break
        numList = line.split(" ")
        if not graph.isConnected(int(numList[0]), int(numList[1])):
                graph.union(int(numList[0]), int(numList[1]))
                print("line: {}  {}".format(numList[0], numList[1]))

    print("Number of Connected Components are: {}".format(graph.connectedComponets()))


if __name__ == "__main__":
    main()
