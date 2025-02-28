<<<<<<< HEAD

# 🌟 **Generador de Contraseñas Seguras y Personalizadas** - Crea contraseñas fuertes y fáciles de recordar

## **Índice**
1. [Descripción](#descripción)
2. [Funciones Principales](#funciones-principales)
   - [Generación Rápida y Personalizada](#generación-rápida-y-personalizada)
   - [Flexibilidad y Control Total](#flexibilidad-y-control-total)
   - [Interfaz Intuitiva y Amigable](#interfaz-intuitiva-y-amigable)
   - [Exportación de Contraseñas](#exportación-de-contraseñas)
3. [Requisitos](#requisitos)
4. [Instalación](#instalación)
5. [Cómo Usar](#cómo-usar)
6. [Contribuciones](#contribuciones)
7. [Arquitectura](#arquitectura)

## **Descripción**

El **Generador de Contraseñas Seguras y Personalizadas** es una herramienta diseñada para crear contraseñas únicas, seguras y fáciles de recordar en cuestión de segundos. Este generador permite la personalización total de las contraseñas con una amplia variedad de caracteres, lo que garantiza un alto nivel de seguridad en línea sin complicaciones. Ideal tanto para usuarios novatos como avanzados, este generador se adapta a tus necesidades de protección digital.

## **Funciones Principales**

### 1. **Generación Rápida y Personalizada**
- **Generación instantánea**: Crea contraseñas aleatorias en cuestión de segundos.
- **Longitud flexible**: Personaliza la longitud de las contraseñas desde 8 hasta 64 caracteres.
- **Variedad de caracteres**: Incluye letras mayúsculas, minúsculas, números y símbolos especiales (`!@#$%^&*`).

### 2. **Flexibilidad y Control Total**
- **Opciones de personalización**: Elige entre contraseñas formadas solo por letras, solo por números o una combinación de ambos.
- **Evita caracteres ambiguos**: El generador tiene la opción de evitar caracteres confusos como `l`, `1`, `O` y `0` para una mayor claridad visual y comprensión.
- **Fácil de recordar y difícil de adivinar**: Genera contraseñas seguras que son fáciles de recordar pero difíciles de adivinar.

### 3. **Interfaz Intuitiva y Amigable**
- **Vista previa**: Muestra una vista previa clara de la contraseña generada antes de finalizar.
- **Diseño minimalista**: Una interfaz sencilla, ideal tanto para principiantes como para usuarios expertos en seguridad.


## **Instalación**

1. **Clonar el repositorio**:
   Abre tu terminal y clona el repositorio del proyecto con el siguiente comando:
   ```bash
   git clone https://tu-repositorio-url.git
   cd generador-contrasenas
   ```

2. **Instalar dependencias**:
   Instala los módulos necesarios utilizando el siguiente comando:
   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecutar el generador de contraseñas**:
   Una vez que las dependencias estén instaladas, ejecuta el script del generador con el siguiente comando:
   ```bash
   python generador_contrasenas.py
   ```

## Arquitectura actual del proyecto
```bash
Random-Password-Generator/
│
│── src/
│   ├── generador.py
│   ├── verificador.py
│   ├── interfaz.py
│── main.py
│── README.md          # Documentación del proyecto
│── requirements.txt          
```

<details>
  <summary><h2>Contribuciones</h2></summary>

¡Las contribuciones son bienvenidas! Si deseas mejorar o añadir nuevas características al proyecto, sigue estos pasos:

1. Haz un **fork** del repositorio.
2. Crea una nueva rama para tu función o corrección:
   ```bash
   git checkout -b nueva-funcion
   ```
3. Realiza los cambios y haz un **commit**:
   ```bash
   git commit -m 'Añadir nueva función'
   ```
4. **Push** los cambios a tu rama en tu repositorio:
   ```bash
   git push origin nueva-funcion
   ```
5. Abre un **Pull Request** en GitHub para que revisemos tus mejoras.

</details>
