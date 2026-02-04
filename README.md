# Design System Documentation Website

Una página web completa para documentar tu design system con navegación por sidebar, tokens de diseño, paletas de colores, tipografía y componentes SaaS.

## 🚀 Inicio Rápido

### Opción 1: Script Automático (Recomendado)

```bash
cd "/Users/besanchez/Downloads/Design system (prueba variables)"
./start-server.sh
```

Luego abre tu navegador en: **http://localhost:8000**

### Opción 2: Comando Manual

```bash
cd "/Users/besanchez/Downloads/Design system (prueba variables)"
python3 -m http.server 8000
```

Luego abre tu navegador en: **http://localhost:8000**

> **Nota**: Es necesario usar un servidor local para que las páginas de Design Tokens y Colores carguen correctamente el archivo JSON (restricciones CORS del navegador).

## 📁 Estructura del Proyecto

```
├── index.html                  - Estructura HTML con sidebar y todas las páginas
├── styles.css                  - Sistema de diseño CSS con variables personalizadas
├── script.js                   - JavaScript para contenido dinámico e interacciones
├── design-system-master.json   - Tokens de diseño (archivo fusionado)
├── start-server.sh            - Script para iniciar el servidor
└── README.md                  - Este archivo
```

## ✨ Características

### Navegación Sidebar
- Diseño limpio y minimalista con gradiente azul oscuro
- Transiciones suaves entre páginas
- Indicadores de estado activo
- Responsive (se colapsa en móviles)

### Páginas Incluidas

#### 🎨 Design Tokens
- Todos los tokens de diseño del archivo JSON
- Previsualizaciones visuales de colores
- Botones para copiar valores
- Organizado por categorías

#### 🌈 Colors
- Paletas completas de colores:
  - Blue (50-1000)
  - Neutral (50-1000)
  - Success (50-1000)
  - Warning (50-1000)
  - Error (50-1000)
  - Basic (white, black)
- Códigos hexadecimales
- Botón de copia en cada color

#### 📝 Typography
- Familias de fuentes: Diagramm (títulos), Roboto (cuerpo)
- Pesos de fuente: Light, Regular, Medium, Bold
- Escala de tamaños dinámicos

#### 🧩 Components
Librería completa de componentes SaaS:
- **Botones**: Primary, Secondary, Outline, Danger, Success, Disabled
- **Campos de entrada**: Text, Email, Password, Textarea
- **Cards**: Con header, body, footer y efectos hover
- **Alertas**: Info, Success, Warning, Error
- **Badges**: Múltiples variantes de color
- **Tabs**: Navegación por pestañas
- **Tablas**: Tablas de datos responsive
- **Modales**: Con backdrop y animaciones
- **Dropdowns**: Menús desplegables
- **Barras de progreso**: Con variantes de color

## 🎯 Funcionalidades Interactivas

- **Copiar al portapapeles**: Click en cualquier botón "Copy" para copiar valores
- **Notificaciones toast**: Confirmación visual al copiar
- **Navegación fluida**: Transiciones suaves entre páginas
- **Efectos hover**: En botones, cards y componentes
- **Estados de foco**: En inputs y elementos interactivos
- **Modal funcional**: Abrir/cerrar con animaciones
- **Dropdown toggle**: Click para abrir/cerrar
- **Tabs interactivos**: Cambio de contenido suave

## 🎨 Sistema de Diseño

### Variables CSS Personalizadas
Todos los tokens convertidos a variables CSS:
```css
--color-blue-600: #365BCA;
--color-success-700: #1B9C67;
--space-16: 16px;
--font-heading: 'Diagramm', sans-serif;
```

### Características de Diseño
- Escala de espaciado unificada
- Radio de borde consistente
- Transiciones y animaciones suaves
- Sombras y elevaciones profesionales
- Diseño responsive

## 📱 Responsive

- Layouts adaptables para móvil
- Sidebar colapsable en pantallas pequeñas
- Sistemas de grid flexibles
- Optimizado para todas las resoluciones

## 🛠️ Tecnologías

- **HTML5**: Estructura semántica
- **CSS3**: Variables personalizadas, Grid, Flexbox
- **JavaScript**: Vanilla JS (sin dependencias)
- **Google Fonts**: Roboto

## 📄 Archivos del Proyecto

- `index.html` - 400+ líneas de HTML estructurado
- `styles.css` - 1000+ líneas de CSS con sistema de diseño completo
- `script.js` - 400+ líneas de JavaScript para funcionalidad
- `design-system-master.json` - 4200+ líneas de tokens de diseño

## 💡 Próximos Pasos (Mejoras Opcionales)

- Añadir funcionalidad de búsqueda/filtro para tokens
- Implementar toggle de modo oscuro
- Añadir snippets de código para cada componente
- Crear archivos descargables de tokens (CSS, SCSS, JSON)
- Incluir documentación de accesibilidad
- Añadir guías de uso para cada componente

## 📞 Soporte

Para cualquier problema o pregunta, consulta la documentación en `walkthrough.md`.

---

**¡Disfruta tu Design System!** 🎉
