# This program reads the contents of the
# philosophers.txt file one line at a time.


def main():
    # Open a file named philosophers.txt.
    infile = open('Chapter_06/philosophers.txt', 'r')

    # Read three lines from the file
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()

    # Close the file.
    infile.close()

    # Print the data that was read into
    # memory.
    print(line1, end="")
    print(line2, end="")
    print(line3, end="")


# Call the main function.
if __name__ == '__main__':
    main()
