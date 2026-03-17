from utils import PaymentHandler, CreditCardHandler, PayPalHandler, CryptoHandler, PaymentProcessor

def main():
    processor = PaymentProcessor()

    # Register supported payment types - no existing code touched
    processor.register("credit", CreditCardHandler())
    processor.register("paypal", PayPalHandler())
    processor.register("crypto", CryptoHandler())

    while True:
        print("\n1. Process Payment")
        print("2. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            processor.process_payment()
        elif choice == "2":
            print("\nNow exiting program.\n")
            break
        else:
            print("\nInvalid Option.")


if __name__ == "__main__":
    main()