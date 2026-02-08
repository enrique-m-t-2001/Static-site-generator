from textnode import TextNode, TextType
import os
import shutil
from copystatic import copy_directory
from generate_page import generate_pages_recursive

def main():
    main_path = os.path.abspath(os.path.dirname(__file__))
    static_path = os.path.join(main_path,"../static")
    public_path = os.path.join(main_path,"../public")
    
    if not os.path.exists(static_path):
        raise FileNotFoundError(f"Directorio 'static' no encontrado: {static_path}")
    if not os.path.isdir(static_path):
        raise NotADirectoryError(f"La ruta {static_path} no es un directorio")
    
    if os.path.exists(public_path):
        shutil.rmtree(public_path)

    os.makedirs(public_path)
    
    copy_directory(static_path,public_path)

    source_path = os.path.join(main_path,"../content/")
    template_path = os.path.join(main_path,"../template.html")
    dest_path = os.path.join(main_path,"../public/")

    generate_pages_recursive(source_path,template_path,dest_path)

 

main()

