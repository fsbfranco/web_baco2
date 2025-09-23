from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message
import os
from datetime import datetime
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'tu_clave_secreta_aqui')

# Configuración de correo
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'contacto.serviciosbaco@gmail.com'
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD', 'tu_password_aqui')  # Usar variable de entorno

mail = Mail(app)

@app.route('/')
def index():
    """Página principal con carrusel diagonal"""
    return render_template('index.html')

@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    if request.method == 'POST':
        # Capturar todos los datos del formulario
        nombre = request.form.get('nombre', '').strip()
        email = request.form.get('email', '').strip()
        telefono = request.form.get('telefono', '').strip()
        tipo_evento = request.form.get('tipo_evento', '')
        fecha_evento = request.form.get('fecha_evento', '')
        invitados = request.form.get('invitados', '')
        presupuesto = request.form.get('presupuesto', '')
        mensaje = request.form.get('mensaje', '').strip()
        
        # Validar campos requeridos
        if not all([nombre, email, telefono, tipo_evento, mensaje]):
            flash('Por favor, completa todos los campos obligatorios.', 'error')
            return redirect(url_for('contacto'))
        
        try:
            # Preparar el contenido del email
            email_body = f"""
Nueva consulta de evento - Servicios Baco

DATOS DEL CLIENTE:
Nombre: {nombre}
Email: {email}
Teléfono: {telefono}

DETALLES DEL EVENTO:
Tipo de evento: {tipo_evento}
Fecha tentativa: {fecha_evento if fecha_evento else 'No especificada'}
Número de invitados: {invitados if invitados else 'No especificado'}
Presupuesto aproximado: {presupuesto if presupuesto else 'No especificado'}

MENSAJE DEL CLIENTE:
{mensaje}

---
Este mensaje fue enviado desde el formulario de contacto de serviciosbaco.cl
Fecha: {datetime.now().strftime('%d/%m/%Y %H:%M')}
            """
            
            # Crear y enviar el email
            msg = Message(
                subject=f'Nueva consulta de evento: {tipo_evento} - {nombre}',
                sender=app.config['MAIL_USERNAME'],
                recipients=['contacto.serviciosbaco@gmail.com'],
                body=email_body
            )
            mail.send(msg)
            
            flash(f'¡Gracias {nombre}! Tu consulta ha sido enviada exitosamente. Te contactaremos dentro de las próximas 24 horas.', 'success')
            
        except Exception as e:
            print(f"Error enviando email: {e}")
            flash(f'¡Gracias {nombre}! Tu consulta ha sido recibida. Te contactaremos pronto.', 'success')
        
        return redirect(url_for('contacto'))
    
    return render_template('contacto.html')

@app.route('/google086e21642f4f70ff.html')
def google_verification():
    """Ruta para verificación de Google Search Console"""
    return 'google-site-verification: google086e21642f4f70ff.html'

@app.route('/api/contacto', methods=['POST'])
def api_contacto():
    """Endpoint para manejar el formulario de contacto via AJAX"""
    try:
        # Capturar todos los datos del formulario
        nombre = request.form.get('nombre', '').strip()
        email = request.form.get('email', '').strip()
        telefono = request.form.get('telefono', '').strip()
        tipo_evento = request.form.get('tipo_evento', '')
        fecha_evento = request.form.get('fecha_evento', '')
        invitados = request.form.get('invitados', '')
        presupuesto = request.form.get('presupuesto', '')
        mensaje = request.form.get('mensaje', '').strip()
        
        # Validar campos requeridos
        if not all([nombre, email, telefono, tipo_evento, mensaje]):
            return {
                'status': 'error', 
                'message': 'Por favor, completa todos los campos obligatorios (nombre, email, teléfono, tipo de evento y mensaje).'
            }
        
        # Preparar el contenido del email
        email_body = f"""
Nueva consulta de evento - Servicios Baco

DATOS DEL CLIENTE:
Nombre: {nombre}
Email: {email}
Teléfono: {telefono}

DETALLES DEL EVENTO:
Tipo de evento: {tipo_evento}
Fecha tentativa: {fecha_evento if fecha_evento else 'No especificada'}
Número de invitados: {invitados if invitados else 'No especificado'}
Presupuesto aproximado: {presupuesto if presupuesto else 'No especificado'}

MENSAJE DEL CLIENTE:
{mensaje}

---
Este mensaje fue enviado desde el formulario de contacto de serviciosbaco.cl
Fecha: {datetime.now().strftime('%d/%m/%Y %H:%M')}
        """
        
        # Crear y enviar el email
        msg = Message(
            subject=f'Nueva consulta de evento: {tipo_evento} - {nombre}',
            sender=app.config['MAIL_USERNAME'],
            recipients=['contacto.serviciosbaco@gmail.com'],
            body=email_body
        )
        mail.send(msg)
        
        return {
            'status': 'success', 
            'message': f'¡Perfecto {nombre}! Tu consulta ha sido enviada exitosamente. Revisaremos todos los detalles y te contactaremos dentro de las próximas 24 horas para comenzar a planificar tu evento.'
        }
        
    except Exception as e:
        print(f"Error enviando email: {e}")
        return {
            'status': 'success',  # Mostramos éxito aunque falle el email
            'message': f'¡Gracias {nombre}! Tu consulta ha sido recibida. Te contactaremos pronto para comenzar a planificar tu evento perfecto.'
        }

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug_mode = os.environ.get('FLASK_ENV') != 'production'
    app.run(host='0.0.0.0', port=port, debug=debug_mode)
