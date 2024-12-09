# YesFitness - Sistema de Gestión de Entrenamientos



YesFitness es un proyecto diseñado para gestionar la selección de entrenamientos físicos de manera sencilla. A través de un menú interactivo, los usuarios pueden elegir los días que desean entrenar, consultar los productos (tipos de entrenamiento) disponibles, ver el costo total de las clases y gestionar su selección. Además, el sistema ofrece una calculadora de IMC (Índice de Masa Corporal) para ayudar a los usuarios a tomar decisiones más informadas sobre su salud y entrenamiento.


## Funcionalidades


1. **Gestión de Productos (Entrenamientos)**:


Los productos (entrenamientos) se cargan en una base de datos SQLite con los detalles: nombre, precio y stock disponible.


El usuario puede ver los productos disponibles y seleccionar el tipo de entrenamiento para los días que desea entrenar.






2. **Cálculo del IMC:**


Si el usuario tiene 18 años o más, puede ingresar su peso y altura para calcular su IMC.


Dependiendo del IMC calculado, el sistema sugiere la frecuencia de entrenamiento (2 a 4 veces por semana, según el rango de IMC).






3. **Selección de Entrenamientos:**


El usuario puede seleccionar entre 1 y 7 días a la semana para entrenar.


Para cada día, el usuario puede elegir un tipo de entrenamiento.


El sistema actualiza el stock de productos cada vez que un usuario selecciona un tipo de entrenamiento.






4. **Visualización y Gestión de Selección:**


El usuario puede ver un resumen de sus días de entrenamiento seleccionados y el total de la compra.


Si lo desea, el usuario puede eliminar una selección y recuperar el stock de ese entrenamiento.






5. **Base de Datos SQLite:**


El proyecto utiliza SQLite para almacenar los productos (tipos de entrenamiento) y los usuarios.


Si no existen productos en la base de datos, se insertan algunos productos predeterminados.








## Estructura del Proyecto


**Clases**


Producto: Representa un tipo de entrenamiento con atributos como id, nombre, precio y stock.


Usuario: Representa al usuario con atributos como nombre, apellido, edad, peso y altura.


Tiene un método para calcular el IMC del usuario.






**Base de Datos**


Se crean dos tablas en SQLite:


productos: Contiene información sobre los tipos de entrenamiento disponibles.


usuarios: Contiene información sobre los usuarios, como nombre, apellido, edad, peso y altura.




**Funciones Principales**


obtener_productos(): Recupera todos los productos de la base de datos.


mostrar_productos(): Muestra todos los productos disponibles en la consola.


actualizar_stock(): Actualiza el stock de un producto cuando es seleccionado por un usuario.


eliminar_producto_seleccionado(): Permite al usuario eliminar un producto de su selección.




**Requisitos**


Para ejecutar este proyecto, asegúrate de tener instalado Python y el módulo sqlite3.


Cómo Ejecutar

1. Clona este repositorio.

2. Abre una terminal y navega hasta el directorio donde se encuentra el archivo.


3. Ejecuta el archivo Python:


**python yesfitness.py**



## Interacción con el Usuario


Al ejecutar el programa, el usuario será recibido con un mensaje de bienvenida y se le pedirá que ingrese su nombre, apellido y edad. A continuación, se le ofrecerá el cálculo de su IMC (si tiene 18 años o más) y podrá elegir los días de entrenamiento que desee. El sistema mostrará las opciones de productos disponibles, permitirá la selección de productos para los días elegidos y actualizará el stock.


El usuario puede borrar una selección de producto si se equivoca.


**Notas**


Este proyecto está diseñado para ser ejecutado en la terminal.


Los productos son tipos de entrenamiento, como "Full Body", "Upper Body", etc., que tienen un precio y un stock predeterminado.



---


| Name   | Last Name    | Email              |
| ------ | ------------ | ------------------ |
| Yesika | Perez Ravelo | yesikapr@gmail.com |

[LinkedIn](https://www.linkedin.com/in/yesikaperezravelo/)

![imagenPerfil](https://firebasestorage.googleapis.com/v0/b/productyesfitness.appspot.com/o/python1.png?alt=media&token=c58f28bc-7f30-4139-abfc-6e16645b5a93)



| Name   | Last Name    | Email              |
| ------ | ------------ | ------------------ |
| Yesika | Perez Ravelo | yesikapr@gmail.com |

[LinkedIn](https://www.linkedin.com/in/yesikaperezravelo/)

![imagenPerfil](https://firebasestorage.googleapis.com/v0/b/productyesfitness.appspot.com/o/python1.png?alt=media&token=c58f28bc-7f30-4139-abfc-6e16645b5a93)

| Yesika | Perez Ravelo | yesikapr@gmail.com |

[LinkedIn](https://www.linkedin.com/in/yesikaperezravelo/)

![imagenPerfil](https://firebasestorage.googleapis.com/v0/b/productyesfitness.appspot.com/o/python1.png?alt=media&token=c58f28bc-7f30-4139-abfc-6e16645b5a93)
