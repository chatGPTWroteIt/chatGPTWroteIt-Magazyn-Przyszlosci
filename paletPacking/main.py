import pandas as pd

class Cuboid:
    width = 0
    height = 0
    depth = 0

    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth


class Package(Cuboid):
    x = 0
    y = 0
    z = 0

    def __init__(self, dimensions, location, depth):
        width, height, depth = dimensions
        super().__init__(self, width, height, depth)

    def addLocation(self, location):
        self.x, self.y, self.z = location


class Pallet(Cuboid):
    packages = []

    def __init__(self):
        super().__init__(800, 1200, 2000 - 144)

    def addPackage(self, package, location):
        package.addLocation(location)
        self.packages.append(package)

def loadPackageTypes():
    packageTypes = pd.read_csv("data/listaProduktow.csv")
    return packageTypes

def loadOrder(orderNo):
    order = pd.read_csv(f"data/Zamowienia/Zamowienie{orderNo}.csv")
    return order

with open("data/file.sth", 'w') as wfile:
    wfile.write("sth")

packages = loadPackageTypes()
print(packages)

packageList = [
    (600, 400, 300),
    (500, 300, 240),
    (800, 600, 400),
    (900, 500, 360),
    (400, 300, 200),
    (600, 400, 360),
    (360, 240, 160),
    (600, 400, 300),
    (800, 600, 400),
    (500, 300, 200),
    (560, 360, 240),
    (440, 320, 200),
    (800, 600, 400),
    (900, 500, 360),
    (360, 240, 160),
    (560, 400, 300),
    (500, 300, 240),
    (800, 600, 400),
    (560, 360, 240),
    (400, 300, 200),
    (360, 200, 160),
]
