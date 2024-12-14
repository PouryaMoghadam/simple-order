# order/serializers.py


class SubmitOrderSerializer:
    """
    Serializer for validating and processing order submissions.
    """

    def __init__(self, data):
        self.data = data
        self.errors = {}
        self.validated_data = {}

    def is_valid(self):
        self._validate_coin()
        self._validate_amount()
        return not self.errors

    def _validate_coin(self):
        coin = self.data.get("coin")
        if not coin:
            self.errors["coin"] = "This field is required."
        elif not isinstance(coin, str):
            self.errors["coin"] = "Coin symbol must be a string."
        else:
            self.validated_data["coin"] = coin.upper()

    def _validate_amount(self):
        amount = self.data.get("amount")
        if amount is None:
            self.errors["amount"] = "This field is required."
        else:
            try:
                amount = float(amount)
                if amount <= 0:
                    self.errors["amount"] = "Amount must be a positive number."
                else:
                    self.validated_data["amount"] = amount
            except (ValueError, TypeError):
                self.errors["amount"] = "Amount must be a number."


class OrderResponseSerializer:
    """
    Serializer for formatting order submission responses.
    """

    def __init__(self, message, order_data=None):
        self.message = message
        self.order_data = order_data

    def serialize(self):
        response = {"message": self.message}
        if self.order_data:
            response["order"] = self.order_data
        return response
