# product.py

def get_product_details(prod_id, name, quantity, price):
    return (
        f"Product ID: {prod_id}\n"
        f"Product Name: {name}\n"
        f"Quantity: {quantity}\n"
        f"Price: {price}"
    )

# Optional manual test
if __name__ == "__main__":
    print(get_product_details(101, "Laptop", 2, 55000))
