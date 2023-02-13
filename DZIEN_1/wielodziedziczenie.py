from abc import ABC, abstractmethod

class MojaAB(ABC):
    def __init__(self,x):
        self.x=x

class ZKlasa(MojaAB):
    def __init__(self, x,y):
        super().__init__(x)
        self.y=y

class DKlasa:
    def __init__(self,g,h):
        self.g=g
        self.h=h

class FKlasa:
    def __init__(self,u):
        self.u=u

class Final(ZKlasa,DKlasa,FKlasa):
    def __init__(self, x, rm, y, u, g, h):
        FKlasa.__init__(self,u)
        DKlasa.__init__(self,g,h)
        ZKlasa.__init__(self,x,y)
        self.rm=rm

    def __repr__(self):
        return f"wartości: x->{self.x}\nrm->{self.rm}\ny->{self.y}\nu->{self.u}\ng->{self.g}\nh->{self.h}\n"

fl = Final(5,7,3,2,1,False)
print(fl)
