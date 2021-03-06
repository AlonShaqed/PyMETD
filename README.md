## PyMETD
Este programa es la interfaz gráfica que corresponde al proyecto final. El programa esta escrito para Python 3. Para poder usar la interfaz gráfica, se reuqiere la librería appJar y para las gráficas se necesita Matplotlib. El programa calcula automáticamente las evaluaciones par-par del modelo AHP. El archivo 'attributes.list' carga en el programa todos los atributos.

### Instalación
Para instalar Python en su computadora, busque el instalador de python 3.x para su sistema operativo. Si usa Linux, posiblemente ya dispone de un compilador nativo (generalmente python3).

Para instalar las librerías necesita el complemento PIP. En la instalación oficial de Python para Windows se instala PIP junto con el compilador. En Linux no cuenta con una instalación por defecto. Se recomienda instalar PIP 3 ($ apt install pip3).
Instale con PIP las librerías necesarias desde la terminal de comandos en su computadora.
Escriba los comandos siguientes, uno a uno:
Windows:
```
> pip install appjar
> pip install matplotlib
```
Linux:
```bash
$ pip3 install appjar
$ pip3 install matplotlib
```

### Ejecución
Desde Windows, puede ejecutar la interfaz gráfica haciendo click doble sobre el archivo **'main.py'** o corriendo desde la línea de comandos.
Desde Linux, es posible que su distribución soporte la ejecución haciendo click doble en el archivo **'main.py'**, pero debe agregarse el permiso para la ejecución ($ chmod +x <archivo>). Pero es más seguro hacerlo desde la línea de comandos:
Todos los SO:
```
$ python main.py
```
