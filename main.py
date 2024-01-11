from paletPacking.main import affordable_rows, transform

import pandas as pd

class Cuboid:
    width = 0
    depth = 0
    height = 0

    def __init__(self, width, depth, height):
        self.width = width
        self.depth = depth
        self.height = height


class Package(Cuboid):
    package = None
    location = None

    def __init__(self, df_package, location):
        self.package = df_package
        self.location = location
        super().__init__(df_package["x"], df_package["y"], df_package["z"])

    def addLocation(self, location):
        self.location = location


class Cursor:
    x = 0
    y = 0
    z = 0

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def copy(self):
        return Cursor(self.x, self.y, self.z)


class Pallet(Cuboid):
    packages = []

    def __init__(self):
        super().__init__(800, 1200, 2000 - 144)

    def addPackage(self, df_package, location):
        package = Package(df_package, location)
        package.addLocation(location)
        self.packages.append(package)


def loadPackageTypes():
    packageTypes = pd.read_csv("data/listaProduktow.csv")
    packageTypes.set_index("ID Produktu", inplace=True)
    packageTypes[['x', 'y','z']] = packageTypes['Wymiary (mm)'].str.split('x', n=2, expand=True)
    packageTypes['x'] = packageTypes['x'].astype(int)
    packageTypes['y'] = packageTypes['y'].astype(int)
    packageTypes['z'] = packageTypes['z'].astype(int)

    packageTypes.drop(columns=['Wymiary (mm)'], inplace=True)


    return packageTypes

def loadOrder(orderNo):
    order = pd.read_csv(f"data/Zamowienia/Zamowienie{orderNo}.csv")
    order.rename(columns={'Ilość': 'count'}, inplace=True)
    return order





def fillRow(pallet, package_row, cursor, rowSize):
    for package_depth in package_row:
        pallet.addPackage(package_depth, cursor, (rowSize[0], package_depth, rowSize[1]))
        cursor.y += package_depth


def fillLayer(pallet, package_layer, cursor, height):
    for width, package_row in package_layer:
        fillRow(pallet, package_row, cursor.copy(), (height, width))
        cursor.x += width


def package_order(raw_row, packages):
    pass


def get_packages(x,y):
    return



pallet = Pallet()
types = loadPackageTypes()

sumaSum = 0
for i in range(1, 21):
    df = loadOrder(i)
    df = df.join(types, on="ID Produktu", how="left", rsuffix="_types")
    size_df = df.drop(
        columns=[
            "Nazwa Produktu_types",
            # "Nazwa Produktu",
            # "Lokacja",
            # "Waga (kg)",
            # "ID Produktu",
        ]
    )
    heights = df["z"].unique()
    cursor = Cursor(0, 0, 0)
    for height in heights:
        flat_df = size_df[size_df["z"] == height]
        widths = flat_df["x"].unique()
        for width in widths:
            curr_df = flat_df[flat_df["x"] == width]

            grouped_df = curr_df.groupby('y')['count'].sum()
            tuples = [(y, count) for y, count in grouped_df.items()]
            row_packages = affordable_rows(df,pallet.width)
            row_packages = transform(row_packages, tuples)

            print(row_packages)
            ordered_df = curr_df.sort_values(by=['Waga (kg)'], ascending=False)
            for components, component_count in row_packages.items():
                for i in range(component_count):
                    for depth,package_count in components:
                        print(f"depth is {depth}")
                        print(ordered_df[ordered_df['y'] == depth])
                        packages_left = 0
                        for j in range(package_count):

                            if(packages_left == 0):
                                counter_df = ordered_df[ordered_df['y'] == depth].iloc[0]
                                packages_left = counter_df['count']
                            packages_left -= 1

                            package = counter_df[['ID Produktu', 'Nazwa Produktu', 'Waga (kg)', 'x', 'y', 'z']]
                            print(f"!!!!!!!!!!!!!! to go:{packages_left}")
                            print(package)
                            pallet.addPackage(package, cursor)
                            cursor.y += depth



            cursor.x += width


        cursor.z += height
        for i in pallet.packages:
            a = i.location
            print(f"!!!{a.x} {a.y} {a.z}!!!")

x = {((200, 6), (300, 0), (260, 0)): 0, ((200, 3), (300, 2), (260, 0)): 0, ((200, 0), (400, 4), (260, 0)): 5},
