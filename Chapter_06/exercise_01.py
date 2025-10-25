def main():
    try:
        #context manager
        with open("Chapter_06/numbers.txt") as infile:
            content = infile.read()
            tokens = content.split()

    except FileNotFoundError as e:
        print(f"The error is: {e}")

    else: 
        if not content:
            print("No data available")
        else:
            print(content)
            print("count: ", len(tokens))
    finally:
        print("Goodbye")

            

#conditional execution
if __name__ == "__main__":
    main()