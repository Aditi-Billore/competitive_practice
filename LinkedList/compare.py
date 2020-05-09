# implementation of linked list and compare the numbers in list
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

    def compare(self, list1, list2):
        temp1 = list1.next
        temp2 = list2.next

        while temp1 != None and temp2 != None:
            if temp1.val != temp2.val:
                return "Different"

            if temp1 is not None: temp1 = temp1.next
            if temp2 is not None: temp2 = temp2.next

        if temp1 == None and temp2 == None:
            return "Same"

        return "Different"

def main():

    list1 = Node()
    list1.create(325)
    list1.print()

    list2 = Node()
    list2.create(325)
    list2.print()

    check = list1.compare(list1,list2)
    print(check)

if __name__ == "__main__":
    main()
