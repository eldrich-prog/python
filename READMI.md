# Pasos para Instalar `requirements.txt` y Crear un Entorno Virtual

## Crear un Entorno Virtual (Opcional)
1. Abre una terminal en el directorio del proyecto.
2. Ejecuta el siguiente comando para crear un entorno virtual:
    ```bash
    python -m venv venv
    ```
3. Activa el entorno virtual:
    - En Windows:
      ```bash
      venv\Scripts\activate
      ```
    - En macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

## Instalar Dependencias desde `requirements.txt`
1. Asegúrate de estar en el entorno virtual (si lo creaste).
2. Ejecuta el siguiente comando para instalar las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

## Verificar Instalación
1. Comprueba que las dependencias se instalaron correctamente:
    ```bash
    pip list
    ```
