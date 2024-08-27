class Tax:
    def __init__(self, rate) -> None:
        self.rate = rate
    
    def getTaxAmount(self, amount):
        return (self.rate / 100) * amount
    
def getTotalAmount(rate, amount):
    tax = Tax(rate)
    tax_amount = tax.getTaxAmount(amount=amount)
    return amount + tax_amount