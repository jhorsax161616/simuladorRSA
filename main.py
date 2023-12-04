from package.utilidades import *
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QFileDialog, QMessageBox

# Cuidado con estos datos
llave_publica_abierta = None
llave_privada_abierta = None

def gui_generar():
    inicio.hide()
    generar.show()
    
def gui_encriptar():
    inicio.hide()
    encriptar.show()
    
def gui_desencriptar():
    inicio.hide()
    desencriptar.show()
    
def btnQueEs():
    inicio.hide()
    queEs.show()
    
def  volver():
    generar.hide()
    encriptar.hide()
    desencriptar.hide()
    queEs.hide()
    inicio.show()
    
# EVENTOS DE GENERAR
def btnGenerarPrimos() -> None:
    bits = 16
    
    p = generar_primo(bits)
    q = generar_primo(bits)
    
    generar.boxPrimer.setText(str(p))
    generar.boxSegun.setText(str(q))
    generar.boxExpo.setText("65537")
    
    limpiarDatosErrores()

def btnGenerarPublica():
    p, q, e = validacionesDeEntrada()
    
    if not p:
        return
    
    if p == q:
        QMessageBox.warning(None, 'Advertencia', 'Los números primos deben ser distintos!!!', QMessageBox.Ok)
        return
    
    phi_n = (p - 1) * (q - 1)
    
    if not validar_exponente_encriptacion(phi_n, e):
        generar.errorPrimo3.setText("Exponente Inválido")
        return
    
    limpiarDatosErrores()
    
    # Generar llave publica
    llave_publica = generar_clave_publica(p, q, e)
    
    # Codificar llave en texto
    publ = llave_a_texto_public(llave_publica)
    
    # Guardar llave en un archivo de texto
    guardarArchivo("llave_publica", publ)
    

def btnGenerarPrivada():
    p, q, e = validacionesDeEntrada()

    if not p:
        return
    
    if p == q:
        QMessageBox.warning(None, 'Advertencia', 'Los números primos deben ser distintos!!!', QMessageBox.Ok)
        return
    
    phi_n = (p - 1) * (q - 1)
    
    if not validar_exponente_encriptacion(phi_n, e):
        generar.errorPrimo3.setText("El exponente de encriptación no es válido")
        return
    
    limpiarDatosErrores()
    
    # Generar llave privada
    llave_privada = generar_clave_privada(p, q, e)
    
    # Codificar llave en texto
    priv = llave_a_texto_private(llave_privada)
    
    # Guardar llave en un archivo de texto
    guardarArchivo("llave_privada", priv)
    
def btnGenerarExponente():
    boxPrimer = generar.boxPrimer.text()
    boxSegun = generar.boxSegun.text()
    # Validando campos vacíos
    if boxPrimer == "":
        generar.errorPrimo1.setText("Rellenar este campo!!!")
        return (False, False, False)
    limpiarDatosErrores()
    if boxSegun == "":
        generar.errorPrimo2.setText("Rellenar este campo!!!")
        return (False, False, False)
    limpiarDatosErrores()
    if not es_numero(boxPrimer):
        generar.errorPrimo1.setText("Este valor no es un número!!!")
        return (False, False, False)
    limpiarDatosErrores()
    if not es_numero(boxSegun):
        generar.errorPrimo2.setText("Este valor no es un número!!!")
        return (False, False, False)
    limpiarDatosErrores()
    # Validar si es primo
    if not es_primo(int(boxPrimer)):
        generar.errorPrimo1.setText("Este no es un número PRIMO!!!")
        return (False, False, False)
    limpiarDatosErrores()
    if not es_primo(int(boxSegun)):
        generar.errorPrimo2.setText("Este no es un número PRIMO!!!")
        return (False, False, False)
    limpiarDatosErrores()
    # Que sean de 3 digitos
    if len(boxPrimer) < 3:
        generar.errorPrimo1.setText("Tiene que ser mayor a 3 dígitos!")
        return (False, False, False)
    limpiarDatosErrores()
    if len(boxSegun) < 3:
        generar.errorPrimo2.setText("Tiene que ser mayor a 3 dígitos!")
        return (False, False, False)
    limpiarDatosErrores()
    if boxPrimer == boxSegun:
        QMessageBox.warning(None, 'Advertencia', 'Los números primos deben ser distintos!!!', QMessageBox.Ok)
        return
    limpiarDatosErrores()
    phi_n = (int(boxPrimer) - 1) * (int(boxSegun) - 1)
    
    try:
        generar.boxExpo.setText(str(generar_exponente_encriptacion(phi_n)))
    except:
        QMessageBox.warning(None, 'Advertencia', 'Seleccione un mayor rango entre los números!', QMessageBox.Ok)
        generar.boxExpo.setText("")

def limpiarDatosErrores() -> None:
    generar.errorPrimo1.setText("")
    generar.errorPrimo2.setText("")
    generar.errorPrimo3.setText("")

def validacionesDeEntrada() -> tuple:
    boxPrimer = generar.boxPrimer.text()
    boxSegun = generar.boxSegun.text()
    boxExpo = generar.boxExpo.text()
    
    # Validando campos vacíos
    if boxPrimer == "":
        generar.errorPrimo1.setText("Rellenar este campo!!!")
        return (False, False, False)
    limpiarDatosErrores()
    if boxSegun == "":
        generar.errorPrimo2.setText("Rellenar este campo!!!")
        return (False, False, False)
    limpiarDatosErrores()
    if boxExpo == "":
        generar.errorPrimo3.setText("Rellenar este campo!!!")
        return (False, False, False)
    limpiarDatosErrores()
    # Validadndo si son números
    if not es_numero(boxPrimer):
        generar.errorPrimo1.setText("Este valor no es un número!!!")
        return (False, False, False)
    limpiarDatosErrores()
    if not es_numero(boxSegun):
        generar.errorPrimo2.setText("Este valor no es un número!!!")
        return (False, False, False)
    limpiarDatosErrores()
    if not es_numero(boxExpo):
        generar.errorPrimo3.setText("Este valor no es un número!!!")
        return (False, False, False)
    limpiarDatosErrores()
    # Que sean de 3 digitos
    if len(boxPrimer) < 3:
        generar.errorPrimo1.setText("Tiene que ser mayor a 3 dígitos!")
        return (False, False, False)
    limpiarDatosErrores()
    if len(boxSegun) < 3:
        generar.errorPrimo2.setText("Tiene que ser mayor a 3 dígitos!")
        return (False, False, False)
    limpiarDatosErrores()
    # Validar si es primo
    if not es_primo(int(boxPrimer)):
        generar.errorPrimo1.setText("Este no es un número PRIMO!!!")
        return (False, False, False)
    limpiarDatosErrores()
    if not es_primo(int(boxSegun)):
        generar.errorPrimo2.setText("Este no es un número PRIMO!!!")
        return (False, False, False)
    limpiarDatosErrores()
    return (int(boxPrimer), int(boxSegun), int(boxExpo))

# EVENTOS DE ENCRIPTAR
def btnSeleccionarPublica():
    global llave_publica_abierta
    try:
        llave_publica_abierta = texto_a_llave(abrirArchivo())
    except:
        llave_publica_abierta = None
def btnEncriptarTexto():
    # Validar si hay llave pública
    if not llave_publica_abierta:
        QMessageBox.warning(None, 'Sin llave pública', 'Seleccione su llave pública!!!', QMessageBox.Ok)
        return
        
    boxTextoEncriptar = encriptar.boxTextoEncriptar.toPlainText()
    
    # Validación texto vacío
    if boxTextoEncriptar == "":
        QMessageBox.warning(None, 'Texto Vacío', 'Ingrese algo de texto por favor', QMessageBox.Ok)
        return
    
    texto_encriptado = cifrar_mensaje(boxTextoEncriptar, llave_publica_abierta)

    encriptar.boxTextoEncriptado.setPlainText(texto_encriptado)
    
def btnExportar():
    boxTextoEncriptado = encriptar.boxTextoEncriptado.toPlainText()
    
    guardarArchivo("texto_encriptado", boxTextoEncriptado)

# EVENTOS DE DESENCRIPTAR
def btnAbrirTexto():
    texto = abrirArchivo()
    desencriptar.boxTextoDesencriptar.setPlainText(texto)
    

def btnSeleccionarPrivada():
    global llave_privada_abierta
    try:
        llave_privada_abierta = texto_a_llave(abrirArchivo())
    except:
        llave_privada_abierta = None

def btnDesencriptarTexto():
    # Validar si hay llave privada
    if not llave_privada_abierta:
        QMessageBox.warning(None, 'Sin llave privada', 'Seleccione su llave privada!!!', QMessageBox.Ok)
        return
    
    boxTextoDesencriptar = desencriptar.boxTextoDesencriptar.toPlainText()
    # Validación texto vacío
    if boxTextoDesencriptar == "":
        QMessageBox.warning(None, 'Texto Vacío', 'Ingrese algo de texto por favor', QMessageBox.Ok)
        return
    try:
        texto_desencriptado = descifrar_mensaje(boxTextoDesencriptar, llave_privada_abierta)
    except:
        desencriptar.boxTextoDesencriptado.setPlainText("##########")    
        QMessageBox.warning(None, 'Advertencia!!!', 'La llave privada no corresponde o la información fue alterada!', QMessageBox.Ok)
        return
    desencriptar.boxTextoDesencriptado.setPlainText(texto_desencriptado)

# FUNCIONES GENERALES
def guardarArchivo(name: str, value: str):
    archivo, _ = QFileDialog.getSaveFileName(None, "Guardar Llave...", f'./{name}.txt', 'Text files (.txt)')
    
    if archivo:
        with open(archivo, 'wt') as f:
            f.write(value)
        
def abrirArchivo():
    archivo, _ = QFileDialog.getOpenFileName(None, 'Abrir Llave...', './', 'Text files (.txt)')
    
    if archivo:
        with open(archivo, 'rt') as f:
            texto = f.read()
            
        return texto
    
    return None

if __name__ == "__main__":
        
    # Iniciando la aplicación
    app = QtWidgets.QApplication([])
    
    # Cargar archivos .ui
    inicio = uic.loadUi('inicio.ui')
    generar = uic.loadUi('generar.ui')
    encriptar = uic.loadUi('encriptar.ui')
    desencriptar = uic.loadUi('desencriptar.ui')
    queEs = uic.loadUi('queEs.ui')
    
    queEs.btnRegresar.clicked.connect(volver)
    
    # Relacionando los Botones de Inicio
    inicio.btnGenerar.clicked.connect(gui_generar)
    inicio.btnEncriptar.clicked.connect(gui_encriptar)
    inicio.btnDesencriptar.clicked.connect(gui_desencriptar)
    inicio.btnQueEs.clicked.connect(btnQueEs)
    
    # Relacionando los Botones de Generar
    generar.btnRegresar.clicked.connect(volver)
    generar.btnGenerarPrimos.clicked.connect(btnGenerarPrimos)
    generar.btnGenerarPublica.clicked.connect(btnGenerarPublica)
    generar.btnGenerarPrivada.clicked.connect(btnGenerarPrivada)
    generar.btnGenerarExponente.clicked.connect(btnGenerarExponente)
    
    
    # Relacionando los Botones de Encriptar
    encriptar.btnRegresar.clicked.connect(volver)
    encriptar.btnSeleccionarPublica.clicked.connect(btnSeleccionarPublica)
    encriptar.btnEncriptarTexto.clicked.connect(btnEncriptarTexto)
    encriptar.btnExportar.clicked.connect(btnExportar)
    
    # Relacionando los Botones de Desencriptar
    desencriptar.btnRegresar.clicked.connect(volver)
    desencriptar.btnAbrirTexto.clicked.connect(btnAbrirTexto)
    desencriptar.btnSeleccionarPrivada.clicked.connect(btnSeleccionarPrivada)
    desencriptar.btnDesencriptarTexto.clicked.connect(btnDesencriptarTexto)
    
    # Ejecutable
    inicio.show()
    app.exec()