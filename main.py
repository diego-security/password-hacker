import secrets
import string
from getpass import getpass
from zxcvbn import zxcvbn


def mostrar_titulo():
    print("\n" + "=" * 48)
    print("             PASSWORD HACKER")
    print("       Password Security Tool")
    print("=" * 48)


def generar_contrasena(longitud):
    minusculas = string.ascii_lowercase
    mayusculas = string.ascii_uppercase
    numeros = string.digits
    simbolos = "!@#$%^&*()-_=+?"

    caracteres = minusculas + mayusculas + numeros + simbolos

    contrasena = [
        secrets.choice(minusculas),
        secrets.choice(mayusculas),
        secrets.choice(numeros),
        secrets.choice(simbolos)
    ]

    for _ in range(longitud - 4):
        contrasena.append(secrets.choice(caracteres))

    secrets.SystemRandom().shuffle(contrasena)

    return "".join(contrasena)


def formato_tiempo(segundos):
    if segundos < 1:
        return "Menos de un segundo / Less than a second"

    unidades = [
        (31536000, "años", "years"),
        (86400, "días", "days"),
        (3600, "horas", "hours"),
        (60, "minutos", "minutes"),
        (1, "segundos", "seconds")
    ]

    for valor, espanol, ingles in unidades:
        if segundos >= valor:
            cantidad = segundos / valor
            numero = f"{cantidad:,.1f}"
            return f"{numero} {espanol} / {numero} {ingles}"

    return "Tiempo no disponible / Time unavailable"


def analizar_contrasena():
    print("\n--- PASSWORD ANALYZER / ANALIZADOR ---")

    contrasena = getpass(
        "Enter password / Escribí tu contraseña: "
    )

    if not contrasena:
        print("Empty password / Contraseña vacía.")
        return

    resultado = zxcvbn(contrasena)

    puntuacion = resultado["score"]

    niveles = [
        "MUY DÉBIL / VERY WEAK",
        "DÉBIL / WEAK",
        "MODERADA / MODERATE",
        "FUERTE / STRONG",
        "MUY FUERTE / VERY STRONG"
    ]

    print("\n--- ANALYSIS RESULTS / RESULTADOS ---")

    print("Security level / Nivel de seguridad:")
    print(niveles[puntuacion])

    print(f"Score / Puntuación: {puntuacion} / 4")

    segundos = resultado["crack_times_seconds"][
        "offline_fast_hashing_1e10_per_second"
    ]

    print("\nEstimated cracking time / Tiempo estimado:")
    print(formato_tiempo(segundos))

    print("\nRecommendations / Recomendaciones:")

    recomendaciones = {
        0: [
            "Use a completely different password. / Usá una contraseña completamente diferente.",
            "Increase length and randomness. / Aumentá la longitud y la aleatoriedad."
        ],
        1: [
            "Add more characters. / Agregá más caracteres.",
            "Avoid common words and patterns. / Evitá palabras comunes y patrones."
        ],
        2: [
            "Use a longer password. / Utilizá una contraseña más larga.",
            "Avoid predictable combinations. / Evitá combinaciones predecibles."
        ],
        3: [
            "Consider increasing its length. / Considerá aumentar su longitud.",
            "Avoid reusing passwords. / Evitá reutilizar contraseñas."
        ],
        4: [
            "No major weaknesses detected. / No se detectaron debilidades importantes.",
            "Never reuse this password. / Nunca reutilices esta contraseña."
        ]
    }

    for recomendacion in recomendaciones[puntuacion]:
        print("- " + recomendacion)

    print("\nIMPORTANT / IMPORTANTE:")
    print(
        "This is an estimate, not a guarantee. / "
        "Es una estimación, no una garantía."
    )


def menu_generador():
    while True:
        print("\n--- PASSWORD GENERATOR / GENERADOR ---")
        print("1. Secure / Segura (16 characters)")
        print("2. Very Secure / Muy segura (20 characters)")
        print("3. Mega Secure / Mega segura (28 characters)")
        print("4. Back / Volver")

        opcion = input("\nSelect / Seleccioná: ")

        longitudes = {
            "1": 16,
            "2": 20,
            "3": 28
        }

        if opcion in longitudes:
            contrasena = generar_contrasena(longitudes[opcion])

            print("\nGenerated password / Contraseña generada:")
            print(contrasena)

            print("\nKeep it safe / Guardala en un lugar seguro.")

        elif opcion == "4":
            break

        else:
            print("Invalid option / Opción inválida.")


def menu_principal():
    while True:
        mostrar_titulo()

        print("\n1. Analyze password / Analizar contraseña")
        print("2. Generate password / Generar contraseña")
        print("3. Exit / Salir")

        opcion = input("\nSelect option / Seleccioná una opción: ")

        if opcion == "1":
            analizar_contrasena()

        elif opcion == "2":
            menu_generador()

        elif opcion == "3":
            print("\nThanks for using Password Hacker!")
            print("¡Gracias por utilizar Password Hacker!")
            break

        else:
            print("Invalid option / Opción inválida.")


if __name__ == "__main__":
    menu_principal()