# implementation of linked list and merge the numbers in list
# two sorted list are given, return new merged list
class Node:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

    def addEnd(self, num):
        newNode = Node(num)
        if self.next is None:
            self.next = newNode
        else:
            temp = self.next
            while temp.next != None:
                temp = temp.next
            temp.next = newNode

    def addBeginning(self, num):
        newNode = Node(num)
        if self.next is None:
            self.next = newNode
        else:
            newNode.next = self.next
            self.next = newNode

    def create(self, num):
        while num > 0:
            self.addBeginning(num%10)
            num = int(num/10)

    def print(self):
        temp = self.next
        while temp!= None:
            print(temp.val, end="")
            temp = temp.next
        print("")

    def getNode(self, positionFromTail):
        current = self.next
        result = self.next
        index = 0

        while current!= None:
            current = current.next
            index += 1

            if index > positionFromTail:
                result = result.next

        return result.val

def main():

    list1 = Node()
    list1.create(567923746)
    list1.print()

    print(list1.getNode(4))

if __name__ == "__main__":
    main()
