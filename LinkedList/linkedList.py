# implementation of linked list and addition of integers in the list in reverse order
class Node:
    # node structure
    # int val: to give one number value
    # Node next: to give next Link

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

    def create(self, num):
        while num / 10 != 0:
            self.addEnd(num%10)
            num = int(num/10)

    def print(self):
        temp = self.next
        while temp!= None:
            print(temp.val, end="")
            temp = temp.next
        print("")

    def __add__(self, otherList):
        #initialise
        temp1 = self.next
        temp2 = otherList.next
        list3 = Node()
        rem = 0

        while temp1 != None or temp2 != None or rem!= 0:
            num1 = 0 if temp1 == None else temp1.val
            num2 = 0 if temp2 == None else temp2.val

            sum = num1 + num2 + rem
            rem = int (sum/10)
            list3.addEnd(sum%10)

            if temp1 is not None: temp1 = temp1.next
            if temp2 is not None: temp2 = temp2.next

        return list3

def main():

    list1 = Node()
    list1.create(5)
    list1.print()

    list2 = Node()
    list2.create(5)
    list2.print()

    list3 = list1 + list2
    list3.print()

if __name__ == "__main__":
    main()
