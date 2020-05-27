class MyQueue(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        while len(self.stack1) > 0:
            self.stack2.append(self.stack1[-1])
            self.stack1.pop()

        self.stack1.append(x)

        while len(self.stack2) > 0:
            self.stack1.append(self.stack2[-1])
            self.stack2.pop()

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if len(self.stack1) > 0:
            return self.stack1.pop()
        return "Queue is empty"

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if len(self.stack1) > 0:
            return self.stack1[-1]
        return "Queue is empty"

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if len(self.stack1) > 0:
            return False
        return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()