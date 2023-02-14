from decimal import Decimal
from akwizytor import Akwizytor
from akwizytornaetacie import AkwizytorNaEtacie

class Boss:
    def __repr__(self):
        return 'Ile zarobi szef wszystkich szefów....'

    def zarobek(self):
        return Decimal('12_000_000.00')

boss = Boss()

s = AkwizytorNaEtacie('Jan','Kowalski','444564',Decimal('756000'),Decimal('4.50'),Decimal('3500'))
c = Akwizytor('Olga','Kot','976565',Decimal('756000'),Decimal('5.3'))

wyplaty = [c,s,boss]

for wp in wyplaty:
    print(wp)
    print(f'{wp.zarobek():,.2f} zł\n')
