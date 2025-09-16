# Servicios Baco - Aplicación Web de Banquetería

Aplicación web Flask moderna y elegante para Servicios Baco, empresa de banquetería familiar con más de 10 años de experiencia. Diseño inspirado en sitios web premium de catering con carrusel dinámico y formulario de contacto completamente funcional.

## ✨ Características Destacadas

- **🎨 Diseño Premium**: Navegación minimalista blanca con efectos elegantes
- **🖼️ Carrusel Dinámico**: 10 imágenes reales de eventos con transiciones suaves
- **📧 Formulario Funcional**: Sistema de contacto con envío real de emails vía Gmail
- **📱 Diseño Responsive**: Optimizado para todos los dispositivos
- **⚡ Navegación Fluida**: Posicionamiento perfecto que ocupa exactamente 100vh
- **🎯 UX Optimizada**: Contenido del hero posicionado estratégicamente

## 🚀 Tecnologías

- **Backend**: Python Flask 3.0.0
- **Email**: Flask-Mail con Gmail SMTP
- **Frontend**: HTML5, CSS3, JavaScript vanilla
- **Estilos**: CSS moderno con efectos glassmorphism
- **Configuración**: python-dotenv para variables de entorno
- **Responsive**: Mobile-first con media queries optimizadas

## 📁 Estructura del Proyecto

```
web_baco2/
├── app.py                          # Aplicación Flask principal
├── requirements.txt                # Dependencias Python
├── .env                           # Variables de entorno (no incluido)
├── .gitignore                     # Archivos ignorados por Git
├── static/
│   └── images/
│       ├── carousel/              # 10 imágenes reales del carrusel
│       └── LogoBaco*.png         # Logos de la empresa
└── templates/
    ├── base.html                  # Template base con navegación
    ├── index.html                 # Página principal con carrusel
    └── contacto.html              # Formulario de contacto funcional
```

## 🛠️ Instalación y Configuración

### 1. Clonar el repositorio
```bash
git clone https://github.com/fsbfranco/web_baco2.git
cd web_baco2
```

### 2. Crear entorno virtual
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Configurar variables de entorno
Crear archivo `.env`:
```env
FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=tu_clave_secreta_aqui
MAIL_USERNAME=contacto.serviciosbaco@gmail.com
MAIL_PASSWORD=tu_app_password_gmail
```

### 5. Ejecutar aplicación
```bash
python app.py
```

### 6. Abrir en navegador
```
http://localhost:5000
```

## 🎨 Características de Diseño

### Navegación
- **Posición**: Fija arriba del carrusel (no flotante)
- **Color**: Blanco elegante con efectos blur
- **Altura**: 50px optimizada para no interferir
- **Efectos**: Hover dorado y líneas animadas
- **Responsive**: Adaptable a móviles (45px/40px)

### Carrusel
- **Altura**: `calc(100vh - 50px)` para ocupar exactamente la pantalla
- **Contenido**: Posicionado al 55% para equilibrio perfecto
- **Imágenes**: 10 fotos reales de eventos con transiciones suaves
- **Botones sociales**: WhatsApp e Instagram perfectamente visibles

### Formulario de Contacto
- **Funcionalidad**: Envío real de emails vía Gmail SMTP
- **Validación**: Frontend y backend completa
- **AJAX**: Respuesta en tiempo real sin recargar página
- **Campos**: Nombre, email, teléfono, tipo de evento, fecha, invitados, mensaje

## 📧 Configuración de Email

Para el formulario de contacto funcional:
1. Crear cuenta de Gmail para la empresa
2. Activar verificación en 2 pasos
3. Generar contraseña de aplicación
4. Configurar variables en `.env`

## 🌟 Últimas Mejoras

- ✅ Navegación cambiada de dorada a blanca con efectos elegantes
- ✅ Posicionamiento perfecto: navegación + carrusel = 100vh exacto
- ✅ Contenido del hero reposicionado para mejor balance visual
- ✅ Eliminados márgenes innecesarios y espacios en blanco
- ✅ Responsive optimizado para todos los dispositivos
- ✅ Botones sociales ajustados para perfecta visibilidad

## 📱 Responsive Design

- **Desktop**: Navegación 50px, carrusel optimizado
- **Tablet**: Navegación 45px, contenido adaptado
- **Mobile**: Navegación 40px, elementos compactos

## 🚀 Comandos Útiles

```bash
# Desarrollo
python app.py

# Producción
flask run --host=0.0.0.0 --port=5000

# Dependencias
pip freeze > requirements.txt
```

## 📞 Información de Contacto

- **Empresa**: Servicios Baco
- **Experiencia**: Más de 10 años en banquetería
- **Especialidad**: Catering, bodas, eventos corporativos
- **Ubicación**: Santiago, Chile
- **Instagram**: [@banquetesbaco](https://www.instagram.com/banquetesbaco/)

## 📄 Licencia

Proyecto privado - Servicios Baco © 2025
