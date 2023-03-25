from CentralBank import *    
from Subscriber import *

cb = CentralBan()

cb.subscribe(Subscriber("Construction Materials Store"))
cb.subscribe(Subscriber("Auto Service \"Victory\""))

cb.setRate("EUR", "USD", 1.2)

print(cb)