import csv


def read_turnovers(filename):
    """
    Reads turnovers from a CSV file and returns a list of values.
    csv.DictReader is a class from Python’s built-in csv
    module. 
    It reads a CSV file and automatically converts each row into a dictionary, using the column headers as keys.
    That means: 
    The first row of your CSV (the header) becomes the dictionary’s keys.
    Each subsequent row becomes a dictionary of key–value pairs.
    """
    turnovers = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                turnovers.append(float(row['Turnover']))
            except ValueError:
                print(f"Skipping invalid entry: {row}")
    return turnovers


def calculate_total(turnovers):
    """Returns the sum of all turnovers."""
    return sum(turnovers)


def main():
    filename = 'Chapter_06/turnovers.csv'
    turnovers = read_turnovers(filename)
    total = calculate_total(turnovers)
    print(f"Total annual turnover: ${total:,.2f}")


if __name__ == "__main__":
    main()
