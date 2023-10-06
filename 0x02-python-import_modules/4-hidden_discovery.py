#!/usr/bin/python3

# Check if this script is being run as the main program
if __name__ == "__main__":
    import hidden_4

    names = dir(hidden_4)

    for name in names:

        if not name.startswith("__"):

            print(name)
