from extract import transform_data


def test_transform_data():
    data = [
        {
            "id": "1",
            "product": "Laptop",
            "quantity": "2",
            "price": "75000"
        }
    ]

    result = transform_data(data)

    assert result[0]["quantity"] == 2
    assert result[0]["price"] == 75000.0
    assert result[0]["total"] == 150000.0