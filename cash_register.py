#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.items = []
        self.previous_transactions = []

        try:
            if discount < 0 or discount > 100:
                raise ValueError
            self.discount = discount
        except Exception:
            self.discount = 0

    def add_item(self, item, price, quantity=1):
        self.total += price * quantity
        for _ in range(quantity):
            self.items.append(item)
        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity,
        })

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
            return

        discounted_total = self.total * (100 - self.discount) / 100
        self.total = discounted_total
        if self.total.is_integer():
            self.total = int(self.total)
        print(f"After the discount, the total comes to ${self.total}.")

    def void_last_transaction(self):
        if not self.previous_transactions:
            return

        last_transaction = self.previous_transactions.pop()
        self.total -= last_transaction["price"] * last_transaction["quantity"]
        for _ in range(last_transaction["quantity"]):
            if self.items:
                self.items.pop()

        if self.total == 0:
            self.total = 0.0
