#Benjamin Diaz

Este proyecto es una herramienta de línea de comandos (CLI) desarrollada en Python para cifrar y descifrar archivos de texto plano utilizando el estándar de encriptación avanzada (AES).

## 🚀 Requisitos Funcionales Cumplidos
- **RF-01:** Control de lectura de archivos de texto (Máximo 1 KB).
- **RF-02:** Generación de llaves criptográficas seguras.
- **RF-03:** Cifrado de contenido (Output: Ciphertext).
- **RF-04:** Descifrado mediante llave original (Recuperación de texto plano).
- **RF-05:** Interfaz de línea de comandos (CLI) funcional.

## 🛠️ Especificaciones Técnicas
- **Librería utilizada:** `pycryptodome`
- **Tamaño de llave:** 256 bits (32 bytes).
- **Algoritmo seleccionado:** AES en modo **EAX**.

### Justificación del Modo AES (EAX)
Se ha seleccionado el modo **EAX** por las siguientes razones:
1. **Autenticidad y Confidencialidad:** A diferencia de modos más simples como CBC, EAX es un modo de "Cifrado Autenticado" (AEAD). Esto significa que no solo protege el contenido, sino que verifica que el archivo no haya sido modificado por un tercero.
2. **Sin Padding:** No requiere rellenar los datos para completar bloques de 16 bytes, lo que simplifica el código y evita ataques de "Padding Oracle".
3. **Detección de Errores:** Si la llave es incorrecta o el archivo cifrado se altera, el algoritmo lanza un error de integridad inmediatamente.

## 📦 Instalación
Para instalar las dependencias necesarias, ejecuta:
```bash
pip install -r requirements.txt
