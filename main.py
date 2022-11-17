class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

    # this function is used to print the objects' data, so if we're using this function, we can avoid
    # print(actual_node.data) 'data' in the print statement and can be given as print(actual_node)
    # but this function converts all data into string to display the stored values

    # def __repr__(self):
    #     return str(self.data)


class LinkedList:
    def __init__(self):
        # this is the first node of the linked list
        # We can access this node exclusively
        self.head = None
        self.num_of_nodes = 0

    # O(1) constant running time
    def insert_start(self, data):
        self.num_of_nodes += 1

        new_node = Node(data)


        # head is null (so the datastructure is empty)
        if self.head is None:
            self.head = new_node

        # so this is when the linked list is not empty
        else:
            # we have to update the references
            new_node.next_node = self.head
            self.head = new_node

    # O(N) running time
    def insert_end(self, data):
        self.num_of_nodes += 1
        new_node = Node(data)

        #  if the linked list is empty
        if self.head is None:
            self.head = new_node
        # this is when the linked list is not empty
        else:
            actual_node = self.head
            # this is why it has O(N) linear running time
            while actual_node.next_node is not None:
                actual_node = actual_node.next_node
                # actual node is the last node. So we insert the new node right after the actual node

            actual_node.next_node = new_node

    # O(N) linear running time
    def remove(self, data):

        # the list is empty
        if self.head is None:
            return

        actual_node = self.head
        # we have to track the previous node for future pointer updates, this is why doubly linked
        # lists are better. we can get the previous node( here with linked lists it is impossible)
        previous_node = None

        # searching for the item that we want to remove(data)
        while actual_node is not None and actual_node.data != data:
            previous_node = actual_node
            actual_node = actual_node.next_node

        # search miss
        if actual_node is None:
            return

        # update the references(so we have the data we want to remove)
        # the head node is the one we want to remove
        if previous_node is None:
            self.head = actual_node.next_node
        else:
            # remove an internal node by updating the pointers
            # No need to delete the node because the garbage collector will do that
            previous_node.next_node = actual_node.next_node



    # O(1) constant running time
    def size_of_list(self):
        return self.num_of_nodes

    def traverse(self):
        actual_node = self.head
        while actual_node is not None:

            print(actual_node.data)
            actual_node = actual_node.next_node


if __name__ == "__main__":

    linkedlist = LinkedList()
    linkedlist.insert_start("adam")
    linkedlist.insert_start("hai")
    linkedlist.insert_start(10)
    linkedlist.remove(10)
    linkedlist.insert_end(15)
    linkedlist.traverse()
