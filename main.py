#==Imports
from appJar import gui
import json
import operator

from misc import *
from ahp import *
from plotit import *

#==========================================================================Backend
def importJson(filepath="proyecto.json"):
	file = open(filepath,"r")
	lines = file.readlines()
	db = []
	for line in lines:
		db.append(json.loads(line))
	return db

def load_labels():
	file = open("attributes.list", "r")
	lines = file.readlines()
	labels = [] #--------Labels & entry names
	for line in lines:
		labels.append(line[:-1].split(","))

	return labels

def load_labels_at(no):
	if type(no) is type(int()):
		labels = load_labels()
		dictl = []

		if no < len(labels):
			for label in labels:
				if label[0] != "$void":
					dictl.append(label[no])

		return dictl
	return False

def load_numerical_labels_at(no):
	if type(no) is type(int()):
		labels = load_labels()
		dictl = []

		if no < len(labels):
			for label in labels:
				if label[0] != "$void" and label[2] == "n":
					dictl.append(label[no])

		return dictl
	return False

def writeToJson(element, path="proyecto.json"):
	if type(element) is type({}):
		file = open(path, "+a")
		file.write(json.dumps(element) + "\n")

def avgs_values():
	dict_ = importJson()
	labels = load_numerical_labels_at(0)
	do_reciprocal = load_numerical_labels_at(4)
	name_tag = load_labels_at(0)[0]
	matrices = []
	pm = None

	for h in range(len(labels)): ####Numerals
		pm = peerMatrix(labels[h], len(dict_))
		for i in range(len(dict_)):
			for j in range(len(dict_)):
				if do_reciprocal[h] == "nr":
					pm.setPeerMatrixAt(i, j, weightAvB(float(dict_[i][labels[h]]), float(dict_[j][labels[h]])))
				elif do_reciprocal[h] == "r":
					pm.setPeerMatrixAt(i, j, weightAvB(reciprocal(float(dict_[i][labels[h]])), reciprocal(float(dict_[j][labels[h]]))))
		matrices.append(pm)
	array = []
	for matrix in matrices:
		matrix.calculateSumVector()
		matrix.calculateNormalizedMatrix()
		matrix.calculateAverageVector()
		array.append(matrix.average)

	avgs = avgMatrix(load_labels_at(0), array)
	avgs.dict()
	avgs.setWeights(load_numerical_labels_at(3))
	avgs.calculateXAvg()
	names_vector = []
	for element in dict_:
		names_vector.append(element[name_tag])
	itemsAvgs = {}
	itemsValues = {}
	for i in range(len(avgs.xAvg)):
		itemsAvgs[names_vector[i]] = avgs.xAvg[i]
	avgs.xMatrix()
	for i in range(len(avgs.xAvg)):
		itemsValues[names_vector[i]] = avgs.xMatrix[i]

	return itemsAvgs, itemsValues
#=============================================================================GUI
menubar = [["Agregar","Cargar"], ["AHP"]]
app = gui("AHP")
#========================================================Promedios
app.startSubWindow("Promedio", modal=True)
app.addLabel("Avgtext", "Esta ventana muestra la tabla de calificaciones promedio de las alternativas.")
app.addLabel("Avgtext1", "La tabla está ordenada hacia abajo de mejor a peor.")
app.addTable("Averages", [["Nombre", "Promedio"]])
app.stopSubWindow()
#==========================================================//
#=========================================================Agregar subwindow
def agregar_elemento(label):
	element = {}
	for label in labels:
		if label[0] != "$void":
			data = app.getEntry(label[0])
			if isfloat(data):
				element[label[0]] = float(data)
			else:
				element[label[0]] = data

	writeToJson(element)
	app.clearAllEntries()


app.startSubWindow("Agregar", modal=True)
no = 0
row = 0
labels = load_labels()
for label in labels:
	app.addLabel("label" + str(no),label[1], row, 0)
	if label[0] != "$void":
		app.addEntry(label[0], row, 1)
	elif label[0] == "$void":
		app.addLabel("void"+str(no))
	no += 1
	row += 1

app.addButton("Agregar", agregar_elemento)
app.stopSubWindow()
#==============================================================//

def agregar():
	app.showSubWindow("Agregar")

def show_element(nombre):
	select = {}
	elements = importJson()
	labels = load_labels()
	for element in elements:
		if element[labels[0][0]] == nombre:
			select = element
			break
	print_= []
	for label in labels:
		if label[0] != "$void":
			print_.append(label[1] + ": " + str(select[label[0]]))
	app.clearListBox("Atributos")
	app.addListItems("Atributos", print_)

def cargar():
	elements = importJson()
	e = 0
	row = 0
	app.setSticky("ew")
	for element in elements:
		try:
			app.addButton(element[labels[0][0]], show_element, row, 0)
		except Exception:
			print("Ya existe el elemento")
			continue
		row += 1
		e += 1

def calcular_AHP():
    averages, values = avgs_values()
    sorted_tuples = sorted(averages.items(), key=operator.itemgetter(1), reverse=True)
    sorted_list = []
    for item in sorted_tuples:
         sorted_list.append(list(item))
    string_list = []
    s= ""
    for item in sorted_list:
        s = ""
        for element in item:
            if element is item[-1]:
                s += str(element)
            else:
                s += str(element) + "  |  "
        string_list.append(s)        
    app.addTableRows("Averages",sorted_list)
    app.showSubWindow("Promedio")
    plot(values, "Atributos", "SOs", "Rendimiento", load_numerical_labels_at(0))
    

def funct_editar(label):
	if label == menubar[0][0]:
		agregar()
	if label == menubar[0][1]:
		cargar()

def funct_calcular(label):
	if label == menubar[1][0]:
		calcular_AHP()

app.setSize(800,500)

#==============================================================Ventana principal
app.addMenuList("Editar", menubar[0], funct_editar)
app.addMenuList("Calcular", menubar[1], funct_calcular)
app.addListBox("Atributos", [], 0,1, colspan=2, rowspan=7)
app.go()
#====================================================================//
