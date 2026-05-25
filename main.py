from forex_python.converter import CurrencyRates
c = CurrencyRates()

def convertCadeur(cad):
    return round(c.convert('CAD' ,'EUR', cad), 2)

def convertCadusd(cad):
    return round(c.convert('CAD' ,'USD', cad), 2)


print(convertCadeur(160), "Euros")
print(convertCadeur(160), "US dollars")


