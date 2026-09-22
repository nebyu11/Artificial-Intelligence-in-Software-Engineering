# Refactored Object-Oriented Product Inventory Manager with Robust Error Handling

class InvalidProductDataError(ValueError):
    """Custom exception raised when invalid product data (negative price or quantity) is assigned."""
    pass


class Product:
    """Represents a product with validated name, price, and quantity using @property getters and setters."""

    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        # Direct assignment triggers @property setters for immediate validation during instantiation
        self.price = price
        self.quantity = quantity

    @property
    def price(self) -> float:
        """Gets the product price."""
        return self._price

    @price.setter
    def price(self, value: float):
        """Sets the product price with non-negative validation."""
        if not isinstance(value, (int, float)) or value < 0:
            raise InvalidProductDataError(f"Invalid price: ${value}. Price must be a non-negative number.")
        self._price = float(value)

    @property
    def quantity(self) -> int:
        """Gets the product quantity."""
        return self._quantity

    @quantity.setter
    def quantity(self, value: int):
        """Sets the product quantity with non-negative validation."""
        if not isinstance(value, int) or value < 0:
            raise InvalidProductDataError(f"Invalid quantity: {value}. Quantity must be a non-negative integer.")
        self._quantity = int(value)


class InventoryManager:
    """Manages the collection of products and provides inventory operations."""

    def __init__(self, inventory=None):
        self.inventory = inventory if inventory is not None else []

    def add_product(self, product: Product):
        """Adds a Product object to the inventory list."""
        if not isinstance(product, Product):
            raise InvalidProductDataError("Only valid Product instances can be added to inventory.")
        self.inventory.append(product)

    def update_quantity(self, name: str, new_quantity: int):
        """Updates the quantity of a product by name."""
        for product in self.inventory:
            if product.name == name:
                # Direct property setter invocation enforces validation
                product.quantity = new_quantity
                return
        print(f"Product '{name}' not found in inventory.")

    def calculate_total_value(self) -> float:
        """Calculates the total monetary value of all inventory."""
        return sum(product.price * product.quantity for product in self.inventory)

    def display_inventory(self):
        """Prints the current inventory list."""
        for product in self.inventory:
            print(f"{product.name} - ${product.price:.2f} x {product.quantity}")


if __name__ == "__main__":
    # Demo Usage
    manager = InventoryManager()
    manager.add_product(Product("Laptop", 1200.00, 5))
    manager.add_product(Product("Mouse", 25.00, 20))
    manager.update_quantity("Mouse", 18)

    print("Current Inventory:")
    manager.display_inventory()
    print(f"\nTotal Inventory Value: ${manager.calculate_total_value():.2f}")

    # Mandatory Test Case: Attempting to set an invalid negative quantity
    print("\n--- Testing Invalid Input ---")
    try:
        manager.inventory[0].quantity = -5
    except Exception as e:
        print(f"Test result: {e}")
