class CentralBan:
    
    def __init__(self):
        self.__rates = {
            "EUR_USD": None,
            "USD_EUR": None,
        }

        self.__subscribers = []

    def subscribe(self, subscriber):
        self.__subscribers.append(subscriber)
    
    def unSubscribe(self, subscriber):
        self.__subscribers.remove(subscriber)

    def notifySubscribers(self):
        for subscriber in self.__subscribers:
            subscriber.update()

    def setRate(self, from_currency, to_currency, rate):
        self.__rates[f"{from_currency}_{to_currency}"] = rate
        self.notifySubscribers()

    def __str__(self):
        return f"BANK RATES: \n{self.__rates} \n{self.__subscribers}"