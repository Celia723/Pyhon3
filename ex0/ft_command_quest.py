import sys

if __name__ == "__main__":
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    num_args = len(sys.argv)
    if (num_args == 1):
        print("No arguments provided!")
    else:
        index = 1
        for arg in sys.argv[1:]:
            print(f"Argument {index}: {arg}")
            index += 1
    print(f"Total arguments: {num_args}")
