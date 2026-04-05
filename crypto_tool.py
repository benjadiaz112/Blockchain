import os
import sys
from Crypto.Cipher import AES  # Corregido: Sin el "dome"
from Crypto.Random import get_random_bytes # Corregido: Sin el "dome"

def generate_key():
    # RF-02: Generar llave de 256 bits (32 bytes)
    return get_random_bytes(32)

def encrypt_file(file_path, key):
    try:
        with open(file_path, 'rb') as f:
            data = f.read()
        
    
        if len(data) > 1024:
            print("Error: El archivo supera el límite de 1 KB.")
            return

        # RF-03: Cifrar usando AES-EAX
        # Se elige EAX porque ofrece confidencialidad y autenticidad sin necesidad de padding.
        cipher = AES.new(key, AES.MODE_EAX)
        ciphertext, tag = cipher.encrypt_and_digest(data)
        
        with open(file_path + ".enc", 'wb') as f:
            [f.write(x) for x in (cipher.nonce, tag, ciphertext)]
        print(f"Archivo cifrado guardado como: {file_path}.enc")
    except FileNotFoundError:
        print("Error: El archivo no existe.")

def decrypt_file(file_path, key):
    try:
        with open(file_path, 'rb') as f:
            # Leemos los componentes: nonce (16 bytes), tag (16 bytes) y el resto es el texto
            nonce, tag, ciphertext = [f.read(x) for x in (16, 16, -1)]

        # RF-04: Descifrar y verificar integridad
        cipher = AES.new(key, AES.MODE_EAX, nonce)
        data = cipher.decrypt_and_verify(ciphertext, tag)
        
        with open(file_path.replace(".enc", ".dec"), 'wb') as f:
            f.write(data)
        print(f"Archivo descifrado con éxito: {file_path.replace('.enc', '.dec')}")
    except ValueError:
        print("Error: La llave es incorrecta o el archivo ha sido alterado.")
    except Exception as e:
        print(f"Error inesperado: {e}")

def main():
    # RF-05: Interfaz de línea de comandos (CLI)
    if len(sys.argv) < 3:
        print("\n--- Herramienta de Criptografía AES ---")
        print("Uso para cifrar: python crypto_tool.py encrypt [archivo]")
        print("Uso para descifrar: python crypto_tool.py decrypt [archivo.enc] [archivo.key]\n")
        return

    mode = sys.argv[1].lower()
    file_name = sys.argv[2]

    if mode == "encrypt":
        key = generate_key()
        # Guardamos la llave para poder descifrar después
        with open("aes_key.key", "wb") as kf:
            kf.write(key)
        encrypt_file(file_name, key)
        print("Llave generada y guardada en: aes_key.key")

    elif mode == "decrypt":
        if len(sys.argv) < 4:
            print("Error: Para descifrar necesitas proporcionar el archivo de la llave.")
            return
        try:
            with open(sys.argv[3], "rb") as kf:
                key = kf.read()
            decrypt_file(file_name, key)
        except FileNotFoundError:
            print("Error: El archivo de llave no existe.")

if __name__ == "__main__":
    main()