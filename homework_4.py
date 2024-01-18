class SavingAccount:
    pass


class ChakingAccount:
    pass


class Stock:
    pass


class Bond:
    pass


class RealEstate:
    pass


class BankAccount(SavingAccount,ChakingAccount):
    pass


class Security(Stock,Bond):
    pass


class InterestBearingItem(BankAccount,Security):
    pass

class Asset(BankAccount,Security,RealEstate):
    pass


class InsurableItem(BankAccount,RealEstate):
    pass


