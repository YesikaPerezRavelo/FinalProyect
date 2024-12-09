import sqlite3

# Class definitions
class Producto:
    def __init__(self, id, nombre, precio, stock):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def __repr__(self):
        return f"Producto({self.id}{self.nombre}, Precio: {self.precio}, Stock: {self.stock})"

class Usuario:
    def __init__(self, nombre, apellido, edad, peso=None, altura=None):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.peso = peso
        self.altura = altura

    def calcular_imc(self):
        if self.peso and self.altura:
            return self.peso / (self.altura ** 2)
        return None

    def __repr__(self):
        return f"Usuario({self.nombre} {self.apellido}, Edad: {self.edad})"

# Crear la conexión a la base de datos
conn = sqlite3.connect('fitness.db')
cursor = conn.cursor()

# Crear tablas en la base de datos si no existen
cursor.execute('''
    CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        precio REAL NOT NULL,
        stock INTEGER NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        apellido TEXT NOT NULL,
        edad INTEGER NOT NULL,
        peso REAL,
        altura REAL
    )
''')

# Verificar si la tabla de productos ya tiene registros
cursor.execute('SELECT COUNT(*) FROM productos')
if cursor.fetchone()[0] == 0:  # Si la tabla está vacía, insertar productos
    productos = [
        Producto(1,"Full Body", 19100, 10),
        Producto(2,"Upper Body", 19100, 10),
        Producto(3,"Lower Body", 19100, 10),
        Producto(4,"Abs", 19100, 10),
        Producto(5,"Yoga", 19100, 10),
        Producto(6,"Stretching", 19100, 10),
        Producto(7,"Aerobics", 19100, 10)
    ]
    cursor.executemany('''
        INSERT INTO productos (nombre, precio, stock)
        VALUES (?, ?, ?)
    ''', [(p.nombre, p.precio, p.stock) for p in productos])
    conn.commit()

    # Verificar si la tabla de usuarios ya tiene registros
cursor.execute('SELECT COUNT(*) FROM usuarios')
if cursor.fetchone()[0] == 0:  # Si la tabla está vacía, insertar usuarios
    usuarios = [
        Usuario("Juan", "Pérez", 25, 70, 1.75),
        Usuario("Ana", "Gómez", 30, 60, 1.65),
        Usuario("Carlos", "Martínez", 28, 80, 1.80),
        Usuario("Lucía", "Rodríguez", 35, 55, 1.60)
    ]
    for usuario in usuarios:
        cursor.execute('''
            INSERT INTO usuarios (nombre, apellido, edad, peso, altura)
            VALUES (?, ?, ?, ?, ?)
        ''', (usuario.nombre, usuario.apellido, usuario.edad, usuario.peso, usuario.altura))
    conn.commit()


# Función para obtener productos desde la base de datos
def obtener_productos():
    cursor.execute('SELECT * FROM productos')
    productos = cursor.fetchall()
    return [Producto(p[0], p[1], p[2], p[3]) for p in productos]

# Función para mostrar productos
def mostrar_productos():
    productos = obtener_productos()
    print("\nProductos disponibles:")
    for producto in productos:
        print(f"ID: {producto.id}, Nombre: {producto.nombre}, Precio: {producto.precio}, Stock: {producto.stock}")

    # for idx, producto in enumerate(productos, start=1):
    #     print(f"{idx}. {producto}")

#Función para borrar producto si se equivoco de su seleccion
# Función para eliminar un producto seleccionado por el usuario
def eliminar_producto_seleccionado():
    if productos_seleccionados:
        print("\nDías seleccionados:")
        for dia, producto in productos_seleccionados.items():
            print(f"{dia}: {producto.nombre}")
        
        dia_a_eliminar = input("Ingresa el día del producto que deseas eliminar: ").lower()
        if dia_a_eliminar in productos_seleccionados:
            producto = productos_seleccionados.pop(dia_a_eliminar)  # Eliminar el producto del diccionario
            # Devolver el stock
            cursor.execute('''
                UPDATE productos
                SET stock = stock + 1
                WHERE nombre = ?
            ''', (producto.nombre,))
            conn.commit()
            print(f"El producto '{producto.nombre}' del día {dia_a_eliminar} ha sido eliminado.")
        else:
            print("No hay un producto asignado a ese día.")
    else:
        print("No tienes productos seleccionados para eliminar.")


# Función para actualizar el stock de un producto
def actualizar_stock(nombre_producto, cantidad):
    cursor.execute('''
        UPDATE productos
        SET stock = stock - ?
        WHERE nombre = ? AND stock >= ?
    ''', (cantidad, nombre_producto, cantidad))
    conn.commit()

# Diccionario para almacenar productos seleccionados
productos_seleccionados = {}

# Mensaje de bienvenida
print("Bienvenido a YesFitness")

# Obtener y guardar datos del usuario
user_name = input("Ingresa tu nombre: ")
user_lastname = input("Ingresa tu apellido: ")
user_age = int(input("Ingresa tu edad: "))  # Convertir la entrada a un entero

usuario = Usuario(user_name, user_lastname, user_age)

print(f"Bienvenido, {usuario.nombre} {usuario.apellido}.")
if usuario.edad >= 18:
    print("Sos mayor de edad.")

    imc_response = input("¿Querés saber tu IMC? Para poder ayudarte mejor en tu selección de entrenamiento (sí/no): ").lower()

    if imc_response in ["sí", "si"]:
        usuario.peso = float(input("Ingresa tu peso en kg: "))
        usuario.altura = float(input("¿Cuál es tu altura en metros? (por ejemplo, 1.75): "))
        imc = usuario.calcular_imc()

        if imc:
            print(f"Tu IMC es {imc:.2f}.")
            if imc < 18.5:
                print("Estás por debajo del peso apropiado. Te recomiendo un nutricionista y un entrenamiento de dos veces por semana.")
            elif imc <= 24.9:
                print("Eres saludable. Te recomiendo un entrenamiento de 4 veces por semana.")
            elif imc <= 29.9:
                print("Tienes sobrepeso. Te recomiendo entrenar 3 veces por semana.")
            elif imc <= 34.9:
                print("Tienes obesidad tipo 1. Te recomiendo entrenar 3 veces por semana.")
            elif imc <= 39.9:
                print("Tienes obesidad tipo 2. Te recomiendo entrenar 3 veces por semana.")
            elif imc >= 40:
                print("Tienes obesidad tipo 3. Te recomiendo entrenar 3 veces por semana.")
        else:
            print("No se pudo calcular el IMC. Verifica tu peso y altura.")

    opcion = 0
    while opcion != 7:
        print("\nMenú de Opciones")
        print("\t1. Mostrar el valor por clase")
        print("\t2. Elegir días de entrenamiento")
        print("\t3. Ver días elegidos y el total")
        print("\t4. Buscar un producto")
        print("\t5. Ver usuario y su selección")
        print("\t6. Borra seleccion")
        print("\t7. Salir")

        opcion = int(input("Seleccioná una opción: "))

        if opcion == 6:
            eliminar_producto_seleccionado()

        elif opcion == 7:
            print("Gracias por usar YesFitness. ¡Hasta pronto!")

        if opcion == 1:
            print(f"El monto por clase es: 19100.")

        elif opcion == 2:
            dias_disponibles = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
            dias_entrenamiento = int(input("¿Cuántos días quieres entrenar por semana? (1-7): "))

            if 1 <= dias_entrenamiento <= 7:
                for i in range(dias_entrenamiento):
                    dia = input(f"Seleccioná el día {i + 1} (lunes a domingo): ").lower()
                    if dia in dias_disponibles:
                        mostrar_productos()
                        tipo_entrenamiento = int(input("Selecciona el número del tipo de entrenamiento: ")) - 1
                        productos = obtener_productos()
                        if 0 <= tipo_entrenamiento < len(productos):
                            producto_seleccionado = productos[tipo_entrenamiento]
                            productos_seleccionados[dia] = producto_seleccionado
                            actualizar_stock(producto_seleccionado.nombre, 1)
                        else:
                            print("Selección no válida.")
                    else:
                        print(f"{dia} no es válido.")
            else:
                print("Número inválido.")

        elif opcion == 3:
            if productos_seleccionados:
                total_costo = sum([p.precio for p in productos_seleccionados.values()])
                print("Días seleccionados:")
                for dia, producto in productos_seleccionados.items():
                    print(f"{dia}: {producto.nombre}")
                print(f"Total: {total_costo}.")
            else:
                print("No has seleccionado ningún día de entrenamiento.")

        elif opcion == 4:
            query = input("Ingresa el nombre del producto: ").lower()
            productos = obtener_productos()
            encontrados = [p for p in productos if query in p.nombre.lower()]
            if encontrados:
                print("Productos encontrados:")
                for p in encontrados:
                    print(p)
            else:
                print("No se encontraron productos.")

        elif opcion == 5:
            print(f"Usuario: {usuario.nombre} {usuario.apellido}, Edad: {usuario.edad}")
            if productos_seleccionados:
                print("Selección de días:")
                for dia, producto in productos_seleccionados.items():
                    print(f"{dia}: {producto.nombre}")
            else:
                print("No has seleccionado días.")

        elif opcion == 6:
            print("Gracias por usar YesFitness. ¡Hasta pronto!")

        else:
            print("Opción no válida.")

# Cerrar la conexión a la base de datos
conn.close()
