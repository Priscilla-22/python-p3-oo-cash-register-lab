#!/usr/bin/env python3


class CashRegister:

    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        for _ in range(quantity):
            self.items.append(title)
        self.last_transaction_amount = price * quantity

    def apply_discount(self):
      if self.discount > 0:
        discount_amount = self.total * (self.discount / 100)
        self.total -= discount_amount
        print(f"After the discount, the total comes to ${int(self.total)}.")
      else:
        print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.last_transaction_amount > 0:
            self.total -= self.last_transaction_amount
            print(f"Last transaction (${self.last_transaction_amount:.2f}) voided.")
            self.last_transaction_amount = 0
        else:
            print("No transactions to void.")

    def reset_register_totals(self):
        self.total = 0
        self.items = []
        self.last_transaction_amount = 0

    def get_price(self, title):
        for item_title, item_price in self.items:
            if item_title == title:
                return item_price
        return 0
