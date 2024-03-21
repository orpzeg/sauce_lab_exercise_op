import re
from decimal import Decimal

from testlibraries.Money import Money


class CurrencyParser:
    @staticmethod
    def parse_currency_and_value(text: str) -> Money:
        """
        Parses the given text to extract a currency symbol and monetary value.

        Args:
            text (str): The text containing the currency symbol and value.

        Returns:
            Optional[Tuple[str, Decimal]]: A tuple containing the currency symbol and the monetary value as a Decimal,
                                           or None if the pattern does not match.
        """
        # Regular expression to match a currency symbol followed by a numeric amount
        match = re.search(r"([\$€£¥])(\d+\.\d{2})", text)

        if match:
            currency_symbol = match.group(1)  # The currency symbol
            amount_str = match.group(2)  # The amount as a string

            # Convert the amount string to a Decimal for precise arithmetic
            amount_decimal = Decimal(amount_str)

            return Money(amount_decimal, currency_symbol)
        else:
            return None
