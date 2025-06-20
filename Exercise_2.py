
class Node:
    def __init__(self, data):
       self.data = data
       self.next = None
 
class Stack(Node):
    def __init__(self):
        self.head = None

    def pop(self):
        if not self.head:
            return

        if not self.head.next:
            val = self.head.data
            self.head = None
            return val

        left = self.head
        right = self.head.next
        while right.next:
            left = right
            right = right.next
        
        left.next = None
        return right.data

    def push(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        

if __name__ == '__main__':
    a_stack = Stack()
    while True:
        #Give input as string if getting an EOF error. Give input like "push 10" or "pop"
        print('push <value>')
        print('pop')
        print('quit')
        do = input('What would you like to do? ').split()
        #Give input as string if getting an EOF error. Give input like "push 10" or "pop"
        operation = do[0].strip().lower()
        if operation == 'push':
            a_stack.push(int(do[1]))
        elif operation == 'pop':
            popped = a_stack.pop()
            if popped is None:
                print('Stack is empty.')
            else:
                print('Popped value: ', int(popped))
        elif operation == 'quit':
            break
