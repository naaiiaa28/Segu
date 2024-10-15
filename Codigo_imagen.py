import os
import hashlib

def comprobarHash():
    fixed_hash = "e5ed313192776744b9b93b1320b5e268"  # Valor Hash de la imagen buscada (nos lo da)
    script_dir = os.path.dirname(__file__)  # Script directory path // directorio del script
    imgs_dir = os.path.join(script_dir, 'imagen')  # Images directory path // directorio de las imagenes

    for img_name in os.listdir(imgs_dir): #loop recorriendo las imagenes
        img_path = os.path.join(imgs_dir, img_name) #ruta de la imagen
        if os.path.isfile(img_path): #si existe la imagen
            with open(img_path, 'rb') as img_file: #abrir la imagen en modo lectura binaria
                img_data = img_file.read()
                img_hash = hashlib.md5(img_data).hexdigest() #aplicar hash a la imagen
                if img_hash == fixed_hash:
                    print(f"Imagen con codigo oculto: {img_name}")
                    break
    else:
        print("No image with the hidden code found.")

# Call the function to execute the task
comprobarHash()