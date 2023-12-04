from package.utilidades import *
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QFileDialog, QMessageBox

# Cuidado con estos datos
llave_publica_abierta = None

def gui_generar():
    inicio.hide()
    generar.show()
    
def gui_encriptar():
    inicio.hide()
    encriptar.show()
    
def gui_desencriptar():
    inicio.hide()
    desencriptar.show()
    
def  volver():
    generar.hide()
    encriptar.hide()
    desencriptar.hide()
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
    
    limpiarDatosErrores()
    
    # Generar llave privada
    llave_privada = generar_clave_privada(p, q, e)
    
    # Codificar llave en texto
    priv = llave_a_texto_private(llave_privada)
    
    # Guardar llave en un archivo de texto
    guardarArchivo("llave_privada", priv)
    

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
    # Validar si es primo
    if not es_primo(int(boxPrimer)):
        generar.errorPrimo1.setText("Este no es un número PRIMO!!!")
        return (False, False, False)
    limpiarDatosErrores()
    if not es_primo(int(boxSegun)):
        generar.errorPrimo2.setText("Este no es un número PRIMO!!!")
        return (False, False, False)
    limpiarDatosErrores()
    if not es_primo(int(boxExpo)):
        generar.errorPrimo3.setText("Este no es un número PRIMO!!!")
        return (False, False, False)
    limpiarDatosErrores()
    return (int(boxPrimer), int(boxSegun), int(boxExpo))

# EVENTOS DE ENCRIPTAR
def btnSeleccionarPublica():
    global llave_publica_abierta
    llave_publica_abierta = texto_a_llave(abrirArchivo())

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

# FUNCIONES GENERALES
def guardarArchivo(name: str, value: str):
    archivo, _ = QFileDialog.getSaveFileName(None, "Guardar Llave...", f'./{name}.txt', 'Text files (.txt)')
    
    with open(archivo, 'wt') as f:
        f.write(value)
        
def abrirArchivo():
    archivo, _ = QFileDialog.getOpenFileName(None, 'Abrir Llave...', './', 'Text files (.txt)')
    
    if archivo:
        with open(archivo, 'rt') as f:
            llave = f.read()
            
        return llave
    
    return None

if __name__ == "__main__":
    """ bits = 16  # Número pequeño para propósitos de demostración
    # Genera claves RSA con primos de 'bits' bits
    p = generar_primo(bits)
    q = generar_primo(bits)
    # Uso del código para generar claves
    llave_publica = generar_clave_publica(p, q)
    llave_privada = generar_clave_privada(p, q)

    print("Llave Pública:", llave_publica)
    print("Llave Privada:", llave_privada)
    
    publ = llave_a_texto_public(llave_publica)
    priv = llave_a_texto_private(llave_privada)
    print(publ)
    print()
    print(priv)
    print()
    print("Llave Pública:", texto_a_llave(publ))
    print("Llave Privada:", texto_a_llave(priv))
    
    mensaje = "Hola mundo"
    
    mencifra = cifrar_mensaje(mensaje, llave_publica)
    print(mencifra)    
    print(f"Descifrado: {descifrar_mensaje(mencifra, llave_privada)}") """
    
    # Iniciando la aplicación
    app = QtWidgets.QApplication([])
    
    # Cargar archivos .ui
    inicio = uic.loadUi('inicio.ui')
    generar = uic.loadUi('generar.ui')
    encriptar = uic.loadUi('encriptar.ui')
    desencriptar = uic.loadUi('desencriptar.ui')
    
    # Relacionando los Botones de Inicio
    inicio.btnGenerar.clicked.connect(gui_generar)
    inicio.btnEncriptar.clicked.connect(gui_encriptar)
    inicio.btnDesencriptar.clicked.connect(gui_desencriptar)
    
    # Relacionando los Botones de Generar
    generar.btnRegresar.clicked.connect(volver)
    generar.btnGenerarPrimos.clicked.connect(btnGenerarPrimos)
    generar.btnGenerarPublica.clicked.connect(btnGenerarPublica)
    generar.btnGenerarPrivada.clicked.connect(btnGenerarPrivada)
    
    
    # Relacionando los Botones de Encriptar
    encriptar.btnRegresar.clicked.connect(volver)
    encriptar.btnSeleccionarPublica.clicked.connect(btnSeleccionarPublica)
    encriptar.btnEncriptarTexto.clicked.connect(btnEncriptarTexto)
    encriptar.btnExportar.clicked.connect(btnExportar)
    
    # Relacionando los Botones de Desencriptar
    desencriptar.btnRegresar.clicked.connect(volver)
    
    # Ejecutable
    inicio.show()
    app.exec()