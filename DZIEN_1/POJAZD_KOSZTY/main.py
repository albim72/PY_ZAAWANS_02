from Pojazd import Pojazd

pj = Pojazd()
odl = 543
lt = 49
cn = 7.61

print(f'spalanie [l/100km]: {pj.spalanie(odl,lt):.2f}')
print(f'koszty przejazdu na trasie {odl} km -> {pj.kosztprzejazdu(odl,lt,cn):.2f} zł')
