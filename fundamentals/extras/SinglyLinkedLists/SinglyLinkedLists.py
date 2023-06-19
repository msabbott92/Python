class SList:
    def __init__(self):
        self.head = None
    def add_to_front(self, val):	# added this line, takes a value
        new_node = SLNode(val)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node

        return self
    
    def add_to_back(self, val):
        new_node = SLNode(val)
        runner = self.head
        while (runner.next != None):
            runner = runner.next
        runner.next = new_node

        return self

    def print_values(self):
        runner = self.head
        while (runner != None):
            print(runner.value)
            runner = runner.next
        return self
    
    def remove_from_front(self):
        if(self.head != None):
            temp = self.head
            self.head = self.head.next
            temp = None


class SLNode:
    def __init__(self, val):
        self.value = val
        self.next = None

my_list = SList()


my_list.add_to_front("jim").add_to_front("dwight").add_to_front("andy").print_values()
my_list.remove_from_front()
my_list.remove_from_back()
my_list.print_values()

