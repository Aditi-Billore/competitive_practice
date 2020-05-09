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

    def merge(self, list1, list2):
        temp1 = list1.next
        temp2 = list2.next
        while temp1 != None and temp2 != None:
            if temp1.val <= temp2.val:
                self.addEnd(temp1.val)
                if temp1 is not None: temp1 = temp1.next
            else:
                self.addEnd(temp2.val)
                if temp2 is not None: temp2 = temp2.next

        while temp1 != None:
            self.addEnd(temp1.val)
            if temp1 is not None: temp1 = temp1.next

        while temp2 != None:
            self.addEnd(temp2.val)
            if temp2 is not None: temp2 = temp2.next

        return

def main():

    list1 = Node()
    list1.create(123)
    list1.print()

    list2 = Node()
    list2.create(34)
    list2.print()

    list3 = Node()
    list3.merge(list1, list2)
    list3.print()

if __name__ == "__main__":
    main()
