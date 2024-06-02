import random
import time

from matplotlib import pyplot as plt
from rbtree import RedBlackTree
from avltree import AVLTree

if __name__ == "__main__":
    num_keys = 100000
    insertion_keys = [random.randint(1, 10000000) for _ in range(num_keys)]
    search_keys = [random.randint(1, 10000000) for _ in range(num_keys)]
    deletion_keys = [random.randint(1, 10000000) for _ in range(num_keys)]

    # Red-Black Tree
    tree = RedBlackTree()
    avl_tree = AVLTree()

    insertion_times_rbtree = []
    deletion_times_rbtree = []
    search_times_rbtree = []

    insertion_times_avl_tree = []
    search_times_avl_tree = []
    deletion_times_avl_tree = []

    # insert elements
    for key in insertion_keys:
        start_time = time.time()
        tree.insert(key)
        end_time = time.time()
        insertion_times_rbtree.append(end_time - start_time)

        start_time = time.time()
        avl_tree.insert(key)
        end_time = time.time()
        insertion_times_avl_tree.append(end_time - start_time)

        start_time = time.time()
        tree.search(key)
        end_time = time.time()
        search_times_rbtree.append(end_time - start_time)

        start_time = time.time()
        avl_tree.search(key)
        end_time = time.time()
        search_times_avl_tree.append(end_time - start_time)

    # Delete elements
    for d_key in insertion_keys:
        start_time = time.time()
        tree.delete(d_key)
        end_time = time.time()
        deletion_times_rbtree.append(end_time - start_time)

        start_time = time.time()
        avl_tree.delete_value(d_key)
        end_time = time.time()
        deletion_times_avl_tree.append(end_time - start_time)
    
    elems = [i for i in range(num_keys)]
    plt.figure(figsize=(10, 6))

    # Inser
    plt.plot(elems, insertion_times_rbtree, label="Red-Black Tree")
    plt.plot(elems, insertion_times_avl_tree, label="AVL Tree")
    plt.xlabel("Number of elements")
    plt.ylabel("Average insertion time per element")
    plt.title("Insertion Time Complexity")
    plt.legend()
    plt.show()

    # Search
    plt.plot(elems, search_times_rbtree, label="Red-Black Tree")
    plt.plot(elems, search_times_avl_tree, label="AVL Tree")
    plt.xlabel("Number of elements")
    plt.ylabel("Average insertion time per element")
    plt.title("Search Time Complexity")
    plt.legend()
    plt.show()

    # Delete
    plt.plot(elems, deletion_times_rbtree, label="Red-Black Tree")
    plt.plot(elems, deletion_times_avl_tree, label="AVL Tree")
    plt.xlabel("Number of elements")
    plt.ylabel("Average insertion time per element")
    plt.title("Delete Time Complexity")
    plt.legend()
    plt.show()
