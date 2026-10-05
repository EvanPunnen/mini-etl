import csv


def extract_data(filename):
    with open(filename, "r") as file:
        data = list(csv.DictReader(file))

    print(f"Rows extracted: {len(data)}")
    return data


def transform_data(data):
    for row in data:
        row["quantity"] = int(row["quantity"])
        row["price"] = float(row["price"])
        row["total"] = row["quantity"] * row["price"]

    return data


if __name__ == "__main__":
    data = extract_data("data/sales.csv")
    data = transform_data(data)

    print(data)