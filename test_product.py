# test_product.py
from product import get_product_details

def test_get_product_details():
    result = get_product_details(101, "Laptop", 2, 55000)

    expected = (
        "Product ID: 101\n"
        "Product Name: Laptop\n"
        "Quantity: 2\n"
        "Price: 55000"
    )

    assert result == expected
