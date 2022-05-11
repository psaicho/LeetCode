
class LinkedNode:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = LinkedNode()

    def append(self, data):
        nextNode = LinkedNode(data)
        if self.head.data == None:
            self.head = nextNode
        else:
            counter = self.head
            while counter.next != None:
                counter = counter.next
            counter.next = nextNode

    def printNode(self):
        counter = self.head
        print(counter.data, "->",counter.next.data)
        while counter.next != None:
            counter = counter.next
            if counter.next != None:
                print(counter.data, "->",counter.next.data)
            else:
                print(counter.data, "-> None")

    def reverseList(self):
        prev = None
        curr = self.head
        while curr:
            next_tmp = curr.next
            curr.next = prev
            prev = curr
            curr = next_tmp
            self.head = prev

    def reverseBetween(self, left: int, right: int):
        curr = self.head
        prev = None
        while curr.data < left:
            curr_head = curr
            curr = curr.next
            print("curr: ", curr.data)

        curr_tail = curr

        while curr.data < right+1:
            next_tmp = curr.next
            curr.next = prev
            prev = curr
            curr = next_tmp
            print("curr: ", curr.data)


class Solution:
    def reverseBetween(self, head, left: int, right: int):
        if head.head.next == None :
            return head
        else:
            licznik = 1
            curr = head.head
            prev = None
            tail = curr

            while licznik < left:
                tail = curr
                curr = curr.next
                licznik += 1
            tail_next = curr

            while licznik < right+1:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
                licznik += 1
            if left == 1:
                head.head = prev
                tail.next = curr
            else:
                tail.next = prev
                tail_next.next = curr
        return head

LL = LinkedList()
lst = [1,3]
for e in lst:
    LL.append(e)
LL.printNode()
Solution.reverseBetween(0,LL,1,2)
print("--------------")
LL.printNode()

# print("licznik w pętli1: ",licznik)
# print("curr: ", curr.data)
# print("licznik: ", licznik)
# print("prev: ", prev.data)
# print("curr_head", curr_head.data)
# print("curr_tail: ", curr_tail.data)
# print("curr: ",curr.data)
# print("licznik: ",licznik)
# print("-----------------")
# print("curr_head: ",curr_head.data)
# print("curr_tail: ", curr_tail.data)


# print("prev: ", prev.data)
#                 if prev.next != None:
#                     print("prev.next: ", prev.next.data)
#                 else:
#                     print("prev.next: None")
#                 print("curr: ", curr.data)
#                 print("curr_head", curr_head.data)
#                 print("curr_tail: ", curr_tail.data)
#                 print("--------------------")
#         print("licznik: ", licznik)
#         print("prev: ", prev.data)
#         if prev.next != None:
#             print("prev.next: ", prev.next.data)
#         else:
#             print("prev.next: None")
#         print("curr: ", curr.data)
#         print("curr_head", curr_head.data)
#         print("curr_tail: ", curr_tail.data)
#         print("curr_tail_next: ", curr_tail_next.data)
#         print("--------------------")