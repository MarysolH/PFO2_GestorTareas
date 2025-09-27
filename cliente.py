import requests

API_URL = "http://127.0.0.1:5000"

def registrar_usuario():
    usuario = input("Ingrese nombre de usuario: ")
    contrasena = input("Ingrese contraseña: ")
    data = {"usuario": usuario, "contraseña": contrasena}
    r = requests.post(f"{API_URL}/registro", json=data)
    print("Respuesta:", r.json())

def iniciar_sesion():
    usuario = input("Usuario: ")
    contrasena = input("Contraseña: ")
    data = {"usuario": usuario, "contraseña": contrasena}
    r = requests.post(f"{API_URL}/login", json=data)
    print("Respuesta:", r.json())

def ver_tareas():
    r = requests.get(f"{API_URL}/tareas")
    if r.status_code == 200:
        print("Página de Tareas recibida:")
        print(r.text)  # muestra el HTML que envía el servidor
    else:
        print("Error:", r.status_code)

def menu():
    while True:
        print("\n===== Cliente API - Gestión de Tareas =====")
        print("1. Registrar usuario")
        print("2. Iniciar sesión")
        print("3. Ver tareas")
        print("0. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            iniciar_sesion()
        elif opcion == "3":
            ver_tareas()
        elif opcion == "0":
            print("Saliendo...")
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    menu()