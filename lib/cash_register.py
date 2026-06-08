#!/usr/bin/env python3

class CashRegister:
    """Simulates a cash register with discount, item tracking, and transaction history."""

    def __init__(self, discount=0):
        """Initialize the register with an optional discount, zero total, and empty lists."""
        self.discount = discount          # triggers setter for validation
        self.total = 0                    # running total of all added items
        self.items = []                   # flat list of all item names added
        self.previous_transactions = []   # history of each transaction as a dict

    @property
    def discount(self):
        """Return the current discount percentage."""
        return self._discount

    @discount.setter
    def discount(self, value):
        """Validate that discount is an integer between 0 and 100 inclusive."""
        if not isinstance(value, int) or not (0 <= value <= 100):
            print("Not valid discount")
        else:
            self._discount = value

    def add_item(self, title, price, quantity=1):
        """Add an item to the register, updating total, items list, and transaction history."""
        # increase total by price times quantity
        self.total += price * quantity

        # add item name to the items list once per quantity
        self.items.extend([title] * quantity)

        # record transaction details for potential void later
        self.previous_transactions.append({
            "title": title,
            "price": price,
            "quantity": quantity
        })

    def apply_discount(self):
        """Apply the discount percentage to the total and print the updated total."""
        if self.discount == 0:
            # no discount set — notify the user
            print("There is no discount to apply.")
        else:
            # calculate and apply the discount
            self.total = self.total - (self.total * self.discount / 100)
            print(f"After the discount, the total comes to ${int(self.total)}.")

    def void_last_transaction(self):
        """Remove the last transaction from history and reverse its effect on total and items."""
        if not self.previous_transactions:
            # nothing to void
            print("There is no transaction to void.")
        else:
            # retrieve the last transaction
            last = self.previous_transactions.pop()

            # subtract its cost from the total
            self.total -= last["price"] * last["quantity"]

            # remove its entries from the items list
            for _ in range(last["quantity"]):
                self.items.remove(last["title"])
