# imports
from os import link
from linked_lists_python import LinkedList

# function definitions


# main function
def main():
    linked_list = LinkedList()

    linked_list.head = -6
    print("ok")
    # linked_list.add_first(4)
    # print("ok")
    # linked_list.add_after(4, 7)

    # linked_list.add_after(linked_list.head, 4)

    print(linked_list)
    return 0


if __name__ == "__main__":
    success = main()
