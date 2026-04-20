def agregar_contacto(agenda):
    nombre = input("Nombre: ")
    telefono = input("Teléfono: ")
    email = input("Email: ")
    # TODO: Crear diccionario y agregarlo a la agenda
    contacto = {"nombre": nombre, "telefono": telefono, "email": email}
    agenda.append(contacto)

def listar_contactos(agenda):
    if not agenda:
        print("Agenda vacía.")
        return
    # TODO: Ordenar por nombre e imprimir en formato tabular
    # Pista: sorted(agenda, key=lambda c: c["nombre"])
    agenda_ordenada = sorted(agenda, key=lambda c: c["nombre"].lower())
    
    print(f"\n{'Nombre':20} {'Teléfono':15} {'Email':25}")
    for c in agenda_ordenada:
        print(f"{c['nombre']:20} {c['telefono']:15} {c['email']:25}")

def buscar_contacto(agenda, termino):
    # TODO: Retornar lista de contactos cuyo nombre contenga 'termino'
    # Pista: usa 'termino.lower() in contacto["nombre"].lower()'
    return [c for c in agenda if termino.lower() in c["nombre"].lower()]

def editar_contacto(agenda):
    nombre = input("Nombre del contacto a editar: ")
    resultados = buscar_contacto(agenda, nombre)
    if not resultados:
        print("No se encontró el contacto.")
        return
    
    # TODO: Si hay múltiples resultados, mostrarlos y pedir selección
    contacto = resultados[0] # Seleccionamos el primero para seguir la lógica base
    
    # TODO: Pedir nuevo teléfono y/o email (enter para no cambiar)
    nuevo_tel = input("Nuevo teléfono (Enter para omitir): ")
    nuevo_email = input("Nuevo email (Enter para omitir): ")
    
    if nuevo_tel:
        contacto["telefono"] = nuevo_tel
    if nuevo_email:
        contacto["email"] = nuevo_email

def eliminar_contacto(agenda):
    nombre = input("Nombre del contacto a eliminar: ")
    # TODO: Buscar y eliminar
    for i, c in enumerate(agenda):
        if c["nombre"].lower() == nombre.lower():
            agenda.pop(i)
            print("Eliminado.")
            return

def exportar_csv(agenda):
    # TODO: Imprimir cada contacto como: nombre,telefono,email
    print("nombre,telefono,email")
    for c in agenda:
        print(f"{c['nombre']},{c['telefono']},{c['email']}")

def estadisticas(agenda):
    # TODO: Total de contactos
    print(f"Total: {len(agenda)}")
    # TODO: Contar dominios de email (parte después del @)
    dominios = [c["email"].split("@")[1] for c in agenda if "@" in c["email"]]
    print(f"Dominios: {set(dominios)}")

def menu():
    agenda = []
    while True:
        print("\n=== AGENDA DE CONTACTOS ===")
        print("1. Agregar contacto")
        print("2. Listar contactos")
        print("3. Buscar contacto")
        print("4. Editar contacto")
        print("5. Eliminar contacto")
        print("6. Exportar CSV")
        print("7. Estadísticas")
        print("8. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            agregar_contacto(agenda)
        elif opcion == "2":
            listar_contactos(agenda)
        elif opcion == "3":
            termino = input("Buscar: ")
            resultados = buscar_contacto(agenda, termino)
            if resultados:
                for c in resultados:
                    print(f"  {c['nombre']} - {c['telefono']} - {c['email']}")
            else:
                print("Sin resultados.")
        elif opcion == "4":
            editar_contacto(agenda)
        elif opcion == "5":
            eliminar_contacto(agenda)
        elif opcion == "6":
            exportar_csv(agenda)
        elif opcion == "7":
            estadisticas(agenda)
        elif opcion == "8":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")

menu()
