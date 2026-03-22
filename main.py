from association import Association
from binary_tree import BinaryTree
import re


def cargar_diccionario(ruta):
    tree = BinaryTree()

    with open(ruta, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            # Ignorar líneas inválidas
            if not line or "," not in line:
                continue

            line = line.replace("(", "").replace(")", "")
            parts = line.split(",")

            if len(parts) != 2:
                continue

            eng = parts[0].strip()
            esp = parts[1].strip()

            tree.insert(Association(eng, esp))

    return tree


def traducir_texto(ruta, tree):
    with open(ruta, "r", encoding="utf-8") as file:
        for line in file:
            palabras = line.split()

            for palabra in palabras:
                limpia = re.sub(r'[^a-zA-Z]', '', palabra).lower()

                resultado = tree.search(limpia)

                if resultado:
                    print(resultado.value, end=" ")
                else:
                    print(f"*{palabra}*", end=" ")
            print()


#  PROGRAMA PRINCIPAL
if __name__ == "__main__":
    arbol = cargar_diccionario("diccionario.txt")

    print(" Diccionario ordenado:")
    arbol.inorder()

    print("\n Traducción:")
    traducir_texto("texto.txt", arbol)