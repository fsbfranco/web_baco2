# Configuración del Formulario de Contacto

## 📧 Configuración de Email

Para que el formulario de contacto funcione correctamente, necesitas configurar el email en Gmail:

### 1. Habilitar verificación en 2 pasos en Gmail
1. Ve a tu cuenta de Google → Seguridad
2. Activa la verificación en 2 pasos

### 2. Generar contraseña de aplicación
1. En Google → Seguridad → Verificación en 2 pasos
2. Busca "Contraseñas de aplicaciones"
3. Genera una nueva para "Servicios Baco Web"
4. Copia la contraseña generada (16 caracteres)

### 3. Configurar variables de entorno
1. Copia `.env.example` como `.env`
2. Completa las variables:
```
MAIL_PASSWORD=tu_password_de_aplicacion_de_16_caracteres
SECRET_KEY=genera_una_clave_secreta_aleatoria
FLASK_ENV=development
```

### 4. Probar el formulario
1. Ejecuta la aplicación: `python app.py`
2. Ve a la página de contacto
3. Llena el formulario completamente
4. Verifica que llegue el email a contacto.serviciosbaco@gmail.com

## 🔧 Funcionalidades implementadas

### Frontend (JavaScript)
- ✅ Validación en tiempo real
- ✅ Envío via AJAX
- ✅ Estados de carga
- ✅ Mensajes de confirmación/error
- ✅ Limpieza automática del formulario
- ✅ Scroll automático al mensaje

### Backend (Flask)
- ✅ Captura de todos los campos del formulario
- ✅ Validación de campos obligatorios
- ✅ Envío de emails con formato profesional
- ✅ Manejo de errores robusto
- ✅ Respuestas JSON para AJAX
- ✅ Fallback en caso de error de email

### Campos del formulario
- ✅ Nombre (obligatorio)
- ✅ Email (obligatorio)
- ✅ Teléfono (obligatorio)
- ✅ Tipo de evento (obligatorio)
- ✅ Fecha tentativa (opcional)
- ✅ Número de invitados (opcional)
- ✅ Presupuesto aproximado (opcional)
- ✅ Mensaje/visión del evento (obligatorio)

### Email enviado incluye:
- Datos completos del cliente
- Detalles específicos del evento
- Fecha y hora de la consulta
- Formato profesional y organizado