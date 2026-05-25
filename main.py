from forex_python.converter import CurrencyRates
c = CurrencyRates()

def convertCadeur(cad):
    return round(c.convert('CAD' ,'EUR', cad), 2)

print(convertCadeur(160), "Euros")


