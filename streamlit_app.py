import streamlit as st

def main():
    st.set_page_config(
        page_title="I Learn Algorithms",
        page_icon="🧮",
        layout="wide"
    )

    st.title("I Learn Algorithms 🧮")
    st.markdown("---")

    # Sidebar for navigation
    st.sidebar.title("Algorithm Categories")
    category = st.sidebar.radio(
        "Select a category:",
        [
            "Arrays & Hashing",
            "Two Pointers",
            "Stack",
            "Binary Search",
            "Sliding Window",
            "Linked List",
            "Trees",
            "Tries",
            "Heap / Priority Queue",
            "Backtracking",
            "Graphs",
            "Advanced Graphs",
            "1-D Dynamic Programming",
            "2-D Dynamic Programming",
            "Greedy",
            "Intervals",
            "Math & Geometry",
            "Bit Manipulation"
        ]
    )

    # Content based on selection
    if category == "Arrays & Hashing":
        st.header("Arrays & Hashing")
        st.write("""
        Arrays and hashing are fundamental data structures and techniques in computer science.
        
        **Arrays:**
        - Collection of elements stored at contiguous memory locations
        - Constant-time access to elements using indices
        - Fixed size in most programming languages
        
        **Hashing:**
        - Technique to map data to fixed-size values
        - Used in hash tables for O(1) average case lookups
        - Common implementations: HashSet, HashMap/Dictionary
        """)

    elif category == "Two Pointers":
        st.header("Two Pointers")
        st.write("""
        The two pointers technique uses two references to traverse an array or sequence.
        
        **Common Applications:**
        - Finding pairs in a sorted array
        - Detecting cycles in linked lists
        - Palindrome verification
        - Container with most water problem
        """)

    elif category == "Stack":
        st.header("Stack")
        st.write("""
        A stack is a LIFO (Last In, First Out) data structure.
        
        **Key Operations:**
        - Push: Add element to top
        - Pop: Remove element from top
        - Peek/Top: View top element
        
        **Common Applications:**
        - Expression evaluation
        - Undo operations
        - Browser history
        - Function call stack
        """)

    elif category == "Binary Search":
        st.header("Binary Search")
        st.write("""
        Binary search is a search algorithm that finds a target value in a sorted array.
        
        **Characteristics:**
        - O(log n) time complexity
        - Requires sorted input
        - Divides search interval in half
        
        **Applications:**
        - Finding elements in sorted arrays
        - Root finding
        - Optimization problems
        """)

    elif category == "Sliding Window":
        st.header("Sliding Window")
        st.write("""
        The sliding window technique is used to solve array/string problems efficiently.
        
        **Types:**
        - Fixed-size window
        - Variable-size window
        
        **Applications:**
        - Maximum sum subarray
        - Longest substring with k distinct characters
        - Finding anagrams in a string
        """)

    elif category == "Linked List":
        st.header("Linked List")
        st.write("""
        A linked list is a linear data structure where elements are stored in nodes.
        
        **Types:**
        - Singly Linked List
        - Doubly Linked List
        - Circular Linked List
        
        **Common Operations:**
        - Insertion
        - Deletion
        - Traversal
        - Reversal
        """)

    elif category == "Trees":
        st.header("Trees")
        st.write("""
        Trees are hierarchical data structures with a root node and child nodes.
        
        **Types:**
        - Binary Trees
        - Binary Search Trees (BST)
        - AVL Trees
        - Red-Black Trees
        
        **Common Operations:**
        - Insertion
        - Deletion
        - Traversal (In-order, Pre-order, Post-order)
        - Search
        """)

    elif category == "Tries":
        st.header("Tries")
        st.write("""
        A trie is a tree-like data structure for storing strings, useful for prefix-based operations.
        
        **Characteristics:**
        - Each node represents a character
        - Paths from root represent strings
        - Efficient prefix operations
        
        **Applications:**
        - Autocomplete
        - Spell checkers
        - IP routing tables
        """)

    elif category == "Heap / Priority Queue":
        st.header("Heap / Priority Queue")
        st.write("""
        A heap is a complete binary tree that satisfies the heap property.
        
        **Types:**
        - Min Heap
        - Max Heap
        
        **Applications:**
        - Priority scheduling
        - Dijkstra's algorithm
        - Median finding
        - Merge K sorted arrays
        """)

    elif category == "Backtracking":
        st.header("Backtracking")
        st.write("""
        Backtracking is an algorithmic technique that solves problems recursively by trying different solutions.
        
        **Characteristics:**
        - Build solution incrementally
        - Remove solutions that fail to satisfy constraints
        
        **Classic Problems:**
        - N-Queens
        - Sudoku Solver
        - Combination Sum
        - Word Search
        """)

    elif category == "Graphs":
        st.header("Graphs")
        st.write("""
        Graphs represent relationships between objects using vertices and edges.
        
        **Representations:**
        - Adjacency Matrix
        - Adjacency List
        
        **Common Algorithms:**
        - BFS (Breadth-First Search)
        - DFS (Depth-First Search)
        - Shortest Path
        - Minimum Spanning Tree
        """)

    elif category == "Advanced Graphs":
        st.header("Advanced Graphs")
        st.write("""
        Advanced graph algorithms solve complex graph problems.
        
        **Algorithms:**
        - Dijkstra's Algorithm
        - Bellman-Ford Algorithm
        - Floyd-Warshall Algorithm
        - Kruskal's Algorithm
        - Prim's Algorithm
        
        **Applications:**
        - Network routing
        - Social networks
        - Game theory
        """)

    elif category == "1-D Dynamic Programming":
        st.header("1-D Dynamic Programming")
        st.write("""
        1-D Dynamic Programming solves problems by breaking them into simpler subproblems.
        
        **Characteristics:**
        - Optimal substructure
        - Overlapping subproblems
        
        **Classic Problems:**
        - Fibonacci sequence
        - Climbing stairs
        - House robber
        - Longest increasing subsequence
        """)

    elif category == "2-D Dynamic Programming":
        st.header("2-D Dynamic Programming")
        st.write("""
        2-D Dynamic Programming uses a two-dimensional array to store subproblem solutions.
        
        **Classic Problems:**
        - Longest Common Subsequence
        - Matrix Chain Multiplication
        - Edit Distance
        - Unique Paths
        """)

    elif category == "Greedy":
        st.header("Greedy Algorithms")
        st.write("""
        Greedy algorithms make locally optimal choices at each step.
        
        **Characteristics:**
        - Make best immediate choice
        - May not lead to global optimal solution
        
        **Common Problems:**
        - Activity Selection
        - Huffman Coding
        - Fractional Knapsack
        - Minimum Coins
        """)

    elif category == "Intervals":
        st.header("Intervals")
        st.write("""
        Interval problems involve ranges or periods with start and end points.
        
        **Common Operations:**
        - Merging intervals
        - Finding overlaps
        - Scheduling
        
        **Applications:**
        - Meeting room scheduling
        - Task scheduling
        - Resource allocation
        """)

    elif category == "Math & Geometry":
        st.header("Math & Geometry")
        st.write("""
        Mathematical and geometric algorithms solve numerical and spatial problems.
        
        **Topics:**
        - Prime Numbers
        - GCD/LCM
        - Geometric Calculations
        - Vector Operations
        
        **Applications:**
        - Computational geometry
        - Computer graphics
        - Mathematical modeling
        """)

    elif category == "Bit Manipulation":
        st.header("Bit Manipulation")
        st.write("""
        Bit manipulation involves operations at the binary level.
        
        **Common Operations:**
        - AND, OR, XOR
        - Bit shifting
        - Setting/clearing bits
        
        **Applications:**
        - Optimization
        - Data compression
        - Error detection/correction
        """)

if __name__ == "__main__":
    main()
