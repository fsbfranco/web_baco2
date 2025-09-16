# Baco - Catering Elegante

Una aplicación web moderna y minimalista para la empresa de catering "Baco", inspirada en el diseño limpio y elegante de catering.com.

## Características

- **Diseño Minimalista**: Inspirado en catering.com con espacios limpios
- **Hero Section Impactante**: Texto prominente y llamadas a la acción
- **Secciones Elegantes**: Frases poderosas y contenido bien estructurado
- **Testimonios**: Reseñas de clientes destacadas
- **Formulario Avanzado**: Sistema de consultas detallado
- **Responsive Design**: Optimizado para todos los dispositivos

## Tecnologías

- **Backend**: Python Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **Estilos**: CSS moderno con Grid y Flexbox
- **Tipografía**: Fuentes elegantes y legibles
- **Responsive**: Mobile-first approach

## Estructura del Proyecto

```
web_baco2/
├── app.py                 # Aplicación principal Flask
├── requirements.txt       # Dependencias Python
├── static/
│   ├── css/
│   │   └── style.css     # Estilos principales
│   ├── js/
│   │   └── main.js       # JavaScript personalizado
│   └── images/           # Imágenes del sitio
└── templates/
    ├── base.html         # Template base
    ├── index.html        # Página de inicio
    └── contacto.html     # Página de contacto
```

## Instalación

1. Crear entorno virtual:
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

2. Instalar dependencias:
```bash
pip install -r requirements.txt
```

3. Ejecutar aplicación:
```bash
python app.py
```

4. Abrir navegador en `http://localhost:5000`

## Configuración

### Variables de Entorno

Crear archivo `.env` con:
```
FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=tu_clave_secreta
MAIL_USERNAME=tu_email@gmail.com
MAIL_PASSWORD=tu_password
```

## Diseño

Inspirado en catering.com, el sitio presenta:
- **Espacios amplios** y diseño limpio
- **Tipografía elegante** con jerarquía clara
- **Colores neutros** con acentos dorados
- **Imágenes de alta calidad** de eventos
- **Navegación intuitiva** y fluida

## Licencia

Proyecto privado - Baco Catering Company
