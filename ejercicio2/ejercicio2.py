import json


# excepcion personalizada
class StockInvalidoError(Exception):
    pass


# clase base
class DispositivoEcológico():

    def __init__(self, codigo: str, nombre: str, precio: float, stock: int):

        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio

        self.__stock = 0
        self.asignar_stock(stock)

    def asignar_stock(self, nuevo_stock):

        if nuevo_stock < 0:
            raise StockInvalidoError("El stock no puede ser negativo")

        self.__stock = nuevo_stock

    def obtener_stock(self):

        return self.__stock

    def mostrar_ficha_tecnica(self):

        return f"Codigo: {self.codigo} | Nombre: {self.nombre} | Precio: ${self.precio} | Stock: {self.obtener_stock()}"


# clase especializada
class PanelSolar(DispositivoEcológico):

    def __init__(self, codigo: str, nombre: str, precio: float, stock: int, potencia_watts: int, eficiencia: float):

        super().__init__(codigo, nombre, precio, stock)

        self.potencia_watts = potencia_watts
        self.eficiencia = eficiencia

    def mostrar_ficha_tecnica(self):

        return f"Codigo: {self.codigo} | Nombre: {self.nombre} | Precio: ${self.precio} | Stock: {self.obtener_stock()} | Potencia: {self.potencia_watts} W | Eficiencia: {self.eficiencia} %"


# gestor del inventario
class GestorInventario():

    def guardar_catalogo_json(self, lista_dispositivos, ruta_archivo):

        catalogo = []

        for dispositivo in lista_dispositivos:

            producto = {
                "codigo": dispositivo.codigo,
                "nombre": dispositivo.nombre,
                "precio": dispositivo.precio,
                "stock": dispositivo.obtener_stock()
            }

            if type(dispositivo) == PanelSolar:

                producto["potencia_watts"] = dispositivo.potencia_watts
                producto["eficiencia"] = dispositivo.eficiencia

            catalogo.append(producto)

        with open(ruta_archivo, "w", encoding="utf-8") as file:
            json.dump(catalogo, file, indent=4, ensure_ascii=False)

        print("Catalogo guardado correctamente.")


# Bloque principal
panel1 = PanelSolar(
    "PS-001",
    "Panel Solar Hogar",
    280_000,
    12,
    450,
    21.8
)

panel2 = PanelSolar(
    "PS-002",
    "Panel Solar Industrial",
    450_000,
    6,
    650,
    23.2
)

dispositivo1 = DispositivoEcológico(
    "DE-001",
    "Inversor Solar",
    190_000,
    9
)

# intento de asignar stock negativo a un producto existente
try:
    panel1.asignar_stock(-5)
except StockInvalidoError as e:
    print(f"Error controlado: {e}")

# intento de crear un producto con stock negativo
try:
    dispositivo2 = DispositivoEcológico(
        "DE-002",
        "Batería de Litio",
        320_000,
        -3
    )
except StockInvalidoError as e:
    print(f"Error controlado: {e}")


# solo se agregan los productos validos
lista_productos = [panel1, panel2, dispositivo1]

print()
print("===== CATALOGO ECOTECH SOLUTIONS =====")

for producto in lista_productos:
    print(producto.mostrar_ficha_tecnica())

print()

gestor = GestorInventario()
gestor.guardar_catalogo_json(lista_productos, "catalogo_ecotech.json")
