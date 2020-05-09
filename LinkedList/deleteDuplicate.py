class Node:
    def __init__(self, data):
        self.val = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def insertAtBeginning(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def create(self, data):
        while data > 0:
            self.insertAtBeginning(data % 10)
            data = data //10

    def print(self):
        temp = self.head
        while temp != None:
            print(temp.val, end=" ")
            temp = temp.next
        print("")

    def deleteDuplicate(self):
        temp = self.head
        prev = self.head
        # initialising temp to second node
        if temp.next == None:
            return
        else:
            temp = temp.next

        while temp.next != None:
            if prev.val == temp.val:
                prev.next = temp.next
                self.print()
            else:
                prev = temp
            temp = temp.next

        if prev.val == temp.val:
            prev.next = None

def main():
    list1 = LinkedList()
    list1.create(1)
    list1.deleteDuplicate()
    list1.print()

if __name__ == "__main__":
    main()
