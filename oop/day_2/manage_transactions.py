from decimal import Decimal


class ManageTran:
    def __int__(self, tran_code: Decimal,
                tran_day: date,
                unit_price: Decimal,
                type: str):
        self.tran_code = tran_code
        self.tran_day = tran_day
        self.unit_price = unit_price
        self.type = type1