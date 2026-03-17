from abc import ABC, abstractmethod

# Abstract base - closed for modification
class PaymentHandler():
    @abstractmethod
    def pay(self, amount: float) -> None:
        pass


# Concrete Handlers - open for extension
class CreditCardHandler(PaymentHandler):
    def pay(self, amount: float) -> None:
        print(f"\n✔ Credit Card payment of ${amount:.2f} processed.")


class PayPalHandler(PaymentHandler):
    def pay(self, amount: float) -> None:
        print(f"\n✔ PayPal payment of ${amount:.2f} processed.")


class CryptoHandler(PaymentHandler):
    def pay(self, amount: float) -> None:
        print(f"\n✔ Crypto payment of ${amount:.2f} processed.")


# Processor is closed for modification - extend by registering new handlers
class PaymentProcessor:
    def __init__(self):
        self.__handlers: dict[str, PaymentHandler] = {}

    def register(self, payment_type: str, handler: PaymentHandler) -> None:
        self.__handlers[payment_type] = handler

    def process_payment(self) -> None:
        payment_type = input(f"\nEnter payment type ({'/'.join(self.__handlers)}): ").lower()
        amount = float(input("Enter payment amount: "))

        handler = self.__handlers.get(payment_type)
        if handler:
            handler.pay(amount)
        else:
            print("Unsupported payment type.\n")