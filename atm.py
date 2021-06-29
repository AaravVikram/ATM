class atm(object):
    def __init__(self, card_number, pin_number):
        self.card_number = card_number
        self.pin_number = pin_number
    
    def cashWithdrawal(self):
        print("Withdrawing Cash")

    def balanceEnquiry(self):
        print("Balancing Enquiry")


withdrawal = atm("3243432", "132123213")
withdrawal.cashWithdrawal()