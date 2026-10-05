import csv

def extract_data(filename):
    with open(filename, "r") as file:
        data = list(csv.DictReader(file))

    print(f"Rows extracted: {len(data)}")
    return data


if __name__ == "__main__":
    extract_data("data/sales.csv")