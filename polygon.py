


class Polygon:
    def __init__(self):
        pass



class Quad(Polygon):
    def __init__(self, sidea, sideb, sidec, sided):
        self.sidea = sidea
        self.sideb = sideb
        self.sidec = sidec
        self.sided = sided
        self.sidelst = sidea, sideb, sidec, sided
    def areasum(self):
        if self.sidea == self.sideb == self.sidec == self.sided:
            area = self.sidea * self.sideb
            return"square with area of",area
        else:
            area = max(self.sidelst) * min(self.sidelst)
            return"rectangle with area of",area

class Tri(Polygon):
    def __init__(self, sidea, sideb, sidec):
        self.sidea = sidea
        self.sideb = sideb
        self.sidec = sidec
        self.semip = (self.sidea + self.sideb + self.sidec/2)
    def areasum(self):
        area = (self.semip * (self.semip - self.sidea) (self.semip - self.sideb) (self.semip - self.sidec)) ** 0.5
        print(area)
        return("area of triangle is %0.2f",area)



shape1 = Quad(14,14,14,14)
shape2 = Quad(47,22,47,22)
shape3 = Tri(15,15,15)
shape4 = Tri(15,10,10)

print(shape1.areasum())
print(shape2.areasum())
print(shape3.areasum())
print(shape4.areasum())

            


        
