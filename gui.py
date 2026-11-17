import tkinter as tk
from tkinter import ttk

from main import generar_contrasena, formato_tiempo
from zxcvbn import zxcvbn

# CONFIGURACIÓN DE LA VENTANA

VENTANA_BG = "#101827"
AZUL = "#1C3553"
VERDE = "#55D99A"
TEXTO = "#A9B8CC"

ventana = tk.Tk()
ventana.title("Password Hacker")
ventana.geometry("850x750")
ventana.configure(bg=VENTANA_BG)

ventana.resizable(False, False)

# TÍTULO PRINCIPAL

titulo = tk.Label(
    ventana,
    text="🛡 PASSWORD HACKER",
    font=("Arial", 25, "bold"),
    bg=VENTANA_BG,
    fg=VERDE
)

titulo.pack(pady=(10, 5))

subtitulo = tk.Label(
    ventana,
    text="PASSWORD SECURITY TOOL",
    font=("Arial", 11),
    bg=VENTANA_BG,
    fg=TEXTO
)

subtitulo.pack()

# SELECTOR DE IDIOMA

idioma = tk.StringVar(value="Español")

# TEXTOS EN ESPAÑOL E INGLES

textos = {
    "Español": {
        "titulo_analisis": "Analizá tu contraseña",
        "descripcion": "Comprobá qué tan resistente es frente a ataques.",
        "etiqueta_password": "Tu contraseña",
        "resultado": "Acá aparecerá el resultado del análisis.",
        "analizar": "ANALIZAR CONTRASEÑA",
        "generador": "Generador de contraseñas",
        "descripcion_generador": "Creá una contraseña aleatoria y segura.",
        "longitud": "Longitud de la contraseña:",
        "caracteres": "caracteres",
        "copiar": "COPIAR CONTRASEÑA",
        "generar": "GENERAR CONTRASEÑA",
        "copiada": "¡Contraseña copiada!",
        "primero": "Primero generá una contraseña.",
        "escribir": "Escribí una contraseña para analizar.",
        "niveles": [
            "MUY DÉBIL",
            "DÉBIL",
            "MODERADA",
            "FUERTE",
            "MUY FUERTE"
        ]
    },

    "English": {
        "titulo_analisis": "Analyze your password",
        "descripcion": "Check how resistant it is to attacks.",
        "etiqueta_password": "Your password",
        "resultado": "The analysis result will appear here.",
        "analizar": "ANALYZE PASSWORD",
        "generador": "Password generator",
        "descripcion_generador": "Create a random and secure password.",
        "longitud": "Password length:",
        "caracteres": "characters",
        "copiar": "COPY PASSWORD",
        "generar": "GENERATE PASSWORD",
        "copiada": "Password copied!",
        "primero": "Generate a password first.",
        "escribir": "Enter a password to analyze.",
        "niveles": [
            "VERY WEAK",
            "WEAK",
            "MODERATE",
            "STRONG",
            "VERY STRONG"
        ]
    }
}

# FUNCION PARA CAMBIAR EL IDIOMA

def cambiar_idioma(event=None):

    t = textos[idioma.get()]

    titulo_analisis.config(text=t["titulo_analisis"])
    descripcion.config(text=t["descripcion"])
    etiqueta_password.config(text=t["etiqueta_password"])
    resultado_analisis.config(text=t["resultado"])
    boton_analizar.config(text=t["analizar"])

    titulo_generador.config(text=t["generador"])
    descripcion_generador.config(text=t["descripcion_generador"])
    etiqueta_longitud.config(text=t["longitud"])

    for opcion in opciones_longitud.winfo_children():
        longitud = int(opcion.cget("value"))
        opcion.config(text=f"{longitud} {t['caracteres']}")

    boton_copiar.config(text=t["copiar"])
    boton_generar.config(text=t["generar"])

    estado_copia.config(text="")

selector_idioma = ttk.Combobox(
    ventana,
    textvariable=idioma,
    values=["Español", "English"],
    state="readonly",
    font=("Arial", 10),
    width=12
)

selector_idioma.place(x=700, y=18, width=110)

# MANTENER ABIERTA LA VENTANA

# PANEL DE ANALISIS

panel_analisis = tk.Frame(
    ventana,
    bg=AZUL,
    padx=25,
    pady=12
)

panel_analisis.pack(
    fill="x",
    padx=40,
    pady=10
)

titulo_analisis = tk.Label(
    panel_analisis,
    text="Analizá tu contraseña",
    font=("Arial", 18, "bold"),
    bg=AZUL,
    fg="white"
)

titulo_analisis.pack(anchor="w")

descripcion = tk.Label(
    panel_analisis,
    text="Comprobá qué tan resistente es frente a ataques.",
    font=("Arial", 10),
    bg=AZUL,
    fg=TEXTO
)

descripcion.pack(anchor="w", pady=(5, 15))

etiqueta_password = tk.Label(
    panel_analisis,
    text="Tu contraseña",
    font=("Arial", 11, "bold"),
    bg=AZUL,
    fg="white"
)

etiqueta_password.pack(anchor="w")

entrada_password = tk.Entry(
    panel_analisis,
    font=("Arial", 13),
    show="*",
    bg="#101827",
    fg="white",
    insertbackground="white",
    relief="flat"
)

entrada_password.pack(fill="x", ipady=10, pady=10)

# RESULTADO DEL ANALISIS

resultado_analisis = tk.Label(
    panel_analisis,
    text="Acá aparecerá el resultado del análisis.",
    font=("Arial", 11),
    bg=AZUL,
    fg=TEXTO,
    justify="left",
    wraplength=700
)

resultado_analisis.pack(anchor="w", pady=15)


# FUNCION PARA ANALIZAR LA CONTRASEÑA

def analizar_desde_ventana():

    password = entrada_password.get()

    if not password:
        resultado_analisis.config(
            text="Escribí una contraseña para analizar.",
            fg="#FF7777"
        )
        return

    analisis = zxcvbn(password)

    puntuacion = analisis["score"]

    niveles = [
        "MUY DEBIL",
        "DEBIL",
        "MODERADA",
        "FUERTE",
        "MUY FUERTE"
    ]

    resultado_analisis.config(
        text=f"Seguridad: {niveles[puntuacion]}",
        fg=VERDE if puntuacion >= 3 else "#FFCC66"
    )


# BOTON PARA ANALIZAR

boton_analizar = tk.Button(
    panel_analisis,
    text="ANALIZAR CONTRASEÑA",
    font=("Arial", 11, "bold"),
    bg=VERDE,
    fg="#101827",
    activebackground="#42C98A",
    activeforeground="#101827",
    relief="flat",
    cursor="hand2",
    command=analizar_desde_ventana
)

boton_analizar.pack(
    fill="x",
    ipady=10,
    pady=(5, 10)
)

# PANEL DEL GENERADOR

panel_generador = tk.Frame(
    ventana,
    bg=AZUL,
    padx=25,
    pady=12
)

panel_generador.pack(
    fill="x",
    padx=40,
    pady=5
)

titulo_generador = tk.Label(
    panel_generador,
    text="Generador de contraseñas",
    font=("Arial", 18, "bold"),
    bg=AZUL,
    fg="white"
)

titulo_generador.pack(anchor="w")

descripcion_generador = tk.Label(
    panel_generador,
    text="Creá una contraseña aleatoria y segura.",
    font=("Arial", 10),
    bg=AZUL,
    fg=TEXTO
)

descripcion_generador.pack(anchor="w", pady=(5, 15))

etiqueta_longitud = tk.Label(
    panel_generador,
    text="Longitud de la contraseña:",
    font=("Arial", 11, "bold"),
    bg=AZUL,
    fg="white"
)

etiqueta_longitud.pack(anchor="w")


# OPCIONES DE LONGITUD

longitud_seleccionada = tk.IntVar(value=20)

opciones_longitud = tk.Frame(
    panel_generador,
    bg=AZUL
)

opciones_longitud.pack(anchor="w", pady=10)

for longitud in [16, 20, 28]:

    opcion = tk.Radiobutton(
        opciones_longitud,
        text=f"{longitud} caracteres",
        variable=longitud_seleccionada,
        value=longitud,
        font=("Arial", 10),
        bg=AZUL,
        fg="white",
        selectcolor="#101827",
        activebackground=AZUL,
        activeforeground=VERDE
    )

    opcion.pack(side="left", padx=(0, 20))


    # CAMPO DE CONTRASEÑA GENERADA

salida_password = tk.Entry(
    panel_generador,
    font=("Arial", 14, "bold"),
    bg="#2ECC71",
    fg="#101827",
    readonlybackground="#2ECC71",
    insertbackground="#101827",
    relief="flat",
    state="readonly",
    justify="center"
)

salida_password.pack(
    fill="x",
    ipady=7,
    pady=5
)


# FUNCION PARA GENERAR CONTRASEÑAS

def generar_desde_ventana():

    longitud = longitud_seleccionada.get()

    nueva_password = generar_contrasena(longitud)

    salida_password.config(state="normal")
    salida_password.delete(0, tk.END)
    salida_password.insert(0, nueva_password)
    salida_password.config(state="readonly")


    # FUNCION PARA COPIAR CONTRASEÑAS

def copiar_desde_ventana():

    password = salida_password.get()

    if not password:
        estado_copia.config(
            text="Primero generá una contraseña.",
            fg="#FFCC66"
        )
        return

    ventana.clipboard_clear()
    ventana.clipboard_append(password)
    ventana.update()

    estado_copia.config(
        text="¡Contraseña copiada!",
        fg=VERDE
    )


    # BOTON PARA COPIAR CONTRASEÑA

estado_copia = tk.Label(
    panel_generador,
    text="",
    font=("Arial", 10),
    bg=AZUL,
    fg=TEXTO
)

estado_copia.pack(pady=1)

boton_copiar = tk.Button(
    panel_generador,
    text="COPIAR CONTRASEÑA",
    font=("Arial", 11, "bold"),
    bg="#1C3553",
    fg="white",
    activebackground="#294B70",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    command=copiar_desde_ventana
)

boton_copiar.pack(
    fill="x",
    ipady=3,
    pady=1
)


# BOTON PARA GENERAR CONTRASEÑA

boton_generar = tk.Button(
    panel_generador,
    text="GENERAR CONTRASEÑA",
    font=("Arial", 11, "bold"),
    bg=VERDE,
    fg="#101827",
    activebackground="#42C98A",
    activeforeground="#101827",
    relief="flat",
    cursor="hand2",
    command=generar_desde_ventana
)

boton_generar.pack(
    fill="x",
    ipady=5,
    pady=2
)



# CONECTAR SELECTOR DE IDIOMA

selector_idioma.bind(
    "<<ComboboxSelected>>",
    cambiar_idioma
)

ventana.mainloop()
