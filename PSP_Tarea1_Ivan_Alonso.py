import psutil


def listar_procesos():
    note_pid = 0
    print("Procesos activos en el sistema:\n")
    for proc in psutil.process_iter():
        try:
            pid = proc.pid
            name = proc.name()
            cpu_usage = proc.cpu_percent()
            memory_usage = proc.memory_percent()
            print(f"PID: {pid} | Nombre: {name} | Uso de CPU: {cpu_usage} | Uso de memoria: {memory_usage}")
            if name == 'Notepad.exe':
                note_pid = pid
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

    if note_pid != 0:
        print(f"El Bloc de notas (Notepad.exe) está en ejecución. PID: {note_pid}")

# De manera alt. podría hacer:

# for proc in psutil.process_iter(['pid', 'name']):
#   try:
#       pid = proc.info['pid']
#       name = proc.info['name']
# Pero es básicamente lo mismo


def finalizar_proceso():
    try:
        pid = int(input("Ingresa el PID del proceso que deseas finalizar: "))
        proceso = psutil.Process(pid)
        proceso.kill()      # (Funciona igual que .terminate(), al menos en windows 11)
        print(f"Proceso con PID {pid} finalizado exitosamente.")
    except psutil.NoSuchProcess:
        print("El proceso no existe.")
    except psutil.AccessDenied:
        print("No tienes permiso para finalizar este proceso.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")


def main():
    while True:
        print("\nOpciones:")
        print("1. Listar todos los procesos activos")
        print("2. Finalizar un proceso por PID")
        print("3. Salir")
        opcion = input("Elige una opción: ")
        if opcion == "1":
            listar_procesos()
        elif opcion == "2":
            finalizar_proceso()
        elif opcion == "3":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intenta nuevamente.")


if __name__ == "__main__":
    main()