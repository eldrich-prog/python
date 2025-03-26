import pywhatkit as kit
import threading
import time 


# Función para enviar el mensaje
def send_message(telefono: str, message: str, hora: int, minuto: int):
    kit.sendwhatmsg(telefono, message, hora, minuto, 5)
    print(f"Mensaje enviado a {telefono}")

if __name__ == "__main__":
    HORA = 16
    MINUTO = 15
    MESSAGE = "HOLA, ESTO ES SPAM"
    TELEFONOS = ["+522271079763","+522271079763"]

    threads = []

    # Crear un hilo para cada teléfono en la lista TELEFONOS
    for telefono in TELEFONOS:
        hilo = threading.Thread(target=send_message, args=(telefono, MESSAGE, HORA, MINUTO))
        threads.append(hilo)
        time.sleep(1)  # Pausa de 1 segundo después de en

    # Iniciar todos los hilos
    for hilo in threads:
        hilo.start()

    # Esperar a que todos los hilos terminen
    for hilo in threads:
        hilo.join()

    print("Todos los mensajes han sido enviados.")
