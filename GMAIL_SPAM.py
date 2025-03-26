import smtplib
from email.message import EmailMessage

# Configuración del remitente
SMTP_SERVER = "smtp.gmail.com"  # Servidor de Gmail
SMTP_PORT = 587  # Puerto para TLS
EMAIL_SENDER = "ingenieroeldrich@gmail.com"
EMAIL_PASSWORD = "vyhe yjsn jlgn qezm"

# Lista de destinatarios con mensajes personalizados
destinatarios = [
    {"email": "notario@notaria7puebla.com.mx", "nombre": "Lic. Adriana Salazar Cajica"},
    {"email": "notaria@34puebla.com", "nombre": "Lic. Antonio Ernesto Zafra Millán"},
    {"email": "contacto@notaria-publica23.com", "nombre": "Lic. Antonio Oropeza Barbosa"},
    {"email": "bcallejo@notaria17puebla.com", "nombre": "Lic. Benjamín De Jesús Del Callejo García"},
    {"email": "edna.jh@notaria37puebla.com", "nombre": "Lic. Carlos Alberto González Cesar"},
    {"email": "carlosbarrientosg@notaria44puebla.com", "nombre": "Lic. Carlos Joaquín Barrientos Granda"},
    {"email": "csc@notaria50puebla.com", "nombre": "Lic. Carlos Roberto Sánchez Castañeda"},
    {"email": "carlos.sanchez@notaria36puebla.com", "nombre": "Lic. Carlos Roberto Sánchez Martínez"},
    {"email": "css@notaria11puebla.com.mx", "nombre": "Lic. Cesar José Sotomayor Sánchez"},
    {"email": "joaquin@notaria46.com.mx", "nombre": "Lic. Ernesto Joaquín Briones Amador"},
    {"email": "glarasaid@notaria19puebla.com", "nombre": "Lic. Fabián Gerardo Lara Said"},
    {"email": "gabriel.ibarra@notaria21puebla.com", "nombre": "Lic. Gabriel Ibarra Romero"},
    {"email": "notaria56puebla@notaria56puebla.com", "nombre": "Lic. Hilda Torres Gómez"},
    {"email": "horacio.hidalgo.mendoza@notariodepuebla.com.mx", "nombre": "Lic. Horacio Hidalgo Mendoza"},
    {"email": "hzurita@notariapublica27.com", "nombre": "Lic. José Hugo Zurita Mercado"},
    {"email": "info@notaria8.com.mx", "nombre": "Lic. José Neyif Irabien Medina"},
    {"email": "n49juridico@notaria49puebla.com", "nombre": "Lic. Juan Carlos Salazar Cajica"},
    {"email": "contacto@notaria48.com.mx", "nombre": "Lic. Luz Verónica Morales Alfaro"},
    {"email": "clientes@notaria54puebla.com.mx", "nombre": "Lic. Marco Antonio Cue Prieto"},
    {"email": "contacto@notaria51pue.com.mx", "nombre": "Lic. Margarita Fernández De Lara Ruiz"},
    {"email": "mcastrocue@notaria18puebla.com.mx", "nombre": "Lic. Mariana Castro Cue Aguilar"},
    {"email": "msalazar@notaria42.com.mx", "nombre": "Lic. Mario Salazar Martínez"},
    {"email": "not39fovissste2@notariapublica39.com", "nombre": "Lic. Raúl Vaquier Ramírez"},
    {"email": "informes@notaria52puebla.com.mx", "nombre": "Lic. Rene Meza Espejel"},
    {"email": "lazcano@notaria40puebla.com", "nombre": "Lic. Reynaldo Lazcano Fernández"},
    {"email": "titular@notaria24puebla.com.mx", "nombre": "Lic. Sergio Moreno Valle German"},
    {"email": "fovinot29@notaria29puebla.com.mx", "nombre": "Lic. Víctor Manuel Aureliano Cortes Padilla"},
    {"email": "creditosfovissste@notariapublica57.com.mx", "nombre": "Lic. Wilma Julián Ruiz"}
]


# Conectar al servidor SMTP
server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
server.starttls()  # Habilitar cifrado TLS
server.login(EMAIL_SENDER, EMAIL_PASSWORD)

# Enviar correos personalizados
for destinatario in destinatarios:
    msg = EmailMessage()
    msg["Subject"] = "Solicitud de Cotización para Escrituración"
    msg["From"] = EMAIL_SENDER
    msg["To"] = destinatario["email"]

    # Mensaje personalizado
    mensaje = f"""
    Estimado {destinatario['nombre']},

    Espero que este mensaje le encuentre bien. Me dirijo a usted con el propósito de solicitar una cotización para la escrituración de un inmueble ubicado en Puebla, Pue. 72070, con un valor de $1,100,000.00 MXN.

    Agradecería que la cotización incluya los siguientes detalles:

    - Honorarios notariales
    - Impuestos y derechos a pagar
    - Gastos administrativos o adicionales
    - Tiempo estimado para la realización del trámite
    - Documentación requerida
    
    Quedo atento a su pronta respuesta y agradezco de antemano su atención. Si requiere información adicional, no dude en comunicarse conmigo.

    Atentamente,
    Eldrich Marin Flores
    2271079763
    ingenieroeldrich@gmail.com
    """
    
    msg.set_content(mensaje)
    server.send_message(msg)  # Enviar correo

# Cerrar conexión con el servidor
server.quit()
print("Correos enviados exitosamente.")
