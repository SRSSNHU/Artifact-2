class PaymentProcessor:
    def process_payment(self):
        payment_type = input("Enter payment type (credit/paypal/crypto): ").lower()
        amount = float(input("Enter payment amount: "))

        if payment_type == "credit":
            print(f"✔ Credit Card payment of ${amount:.2f} processed.\n")
        elif payment_type == "paypal":
            print(f"✔ PayPal payment of ${amount:.2f} processed.\n")
        elif payment_type == "crypto":
            print(f"✔ Crypto payment of ${amount:.2f} processed.\n")
        else:
            print("Unsupported payment type.\n")

    def process_credit(self, amount):
        print(f"Processing credit card payment of ${amount}\n")

    def process_paypal(self, amount):
        print(f"Processing PayPal payment of ${amount}\n")

    def process_crypto(self, amount):
        print(f"Processing crypto payment of ${amount}\n")


def main():
    processor = PaymentProcessor()

    while True:
        print("1. Process Payment")
        print("2. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            processor.process_payment()
        elif choice == "2":
            break
        else:
            print("Invalid option.\n")


if __name__ == "__main__":
    main()