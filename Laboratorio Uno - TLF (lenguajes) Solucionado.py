import random
import tkinter as tk
from tkinter import messagebox

#Variables globales para manejar las operaciones
languages = []
alphabet = []
result = []

# Función que pide al usuario la información necesaria, osea el alfabeto y la cantidad
def define_alphabet_and_languages():
    global alphabet, languages
    alphabet = []
    
    try:
        # Se pide la cantidad de elementos del alfabeto
        alphabet_size = int(entry_alphabet_size.get())
        
        # se pide el alfabeto separado por comas para luego hacer SPLIT
        alphabet_input = entry_alphabet_elements.get()
        alphabet = alphabet_input.split(",")  # Dividir la cadena en elementos separados por comas
        
        # Valida que el número de elementos sea el correcto
        if len(alphabet) != alphabet_size:
            raise ValueError("El número de elementos no coincide con el tamaño del alfabeto ingresado.")
        
        # Crear los lenguajes a partir del alfabeto, crea 3

        #PUNTO 1
        partition_size = max(1, alphabet_size // 3)
        languages = [
            alphabet[:partition_size],
            alphabet[partition_size: 2 * partition_size],
            alphabet[2 * partition_size:]
        ]
        
        messagebox.showinfo("Lenguajes Definidos", f"Lenguaje 1: {languages[0]}\nLenguaje 2: {languages[1]}\nLenguaje 3: {languages[2]}")
    
    except ValueError as ve:
        messagebox.showerror("Error", f"Error: {ve}")

# Funciones en general con todas las operaciónes

# PUNTO 2
#Unión
def union_languages():
    global result
    result = list(set(languages[0] + languages[1] + languages[2]))
    messagebox.showinfo("Resultado de Unión", f"Resultado: {', '.join(result)}")
#concatenación
def concatenation_languages():
    global result
    result = [a + b for a in languages[0] for b in languages[1]]
    messagebox.showinfo("Resultado de Concatenación", f"Resultado: {', '.join(result)}")
#Estrella
def kleene_star(language):
    global result
    result = ['']
    for _ in range(3):
        result += [a + b for a in language for b in result]
    result = list(set(result))
    messagebox.showinfo("Resultado de Estrella de Kleene", f"Resultado: {', '.join(result)}")

# Funciones para generar y verificar palíndromos 
#Punto 3
def generate_palindrome():
    random_length = random.randint(1, len(alphabet) // 2)
    half = ''.join(random.choice(alphabet) for _ in range(random_length))
    palindrome = half + half[::-1]
    messagebox.showinfo("Palíndromo Generado", f"Palíndromo: {palindrome}")
#PUNTO 4, verifica si una cadena es palíndorma
def check_palindrome():
    user_input = entry_palindrome.get()
    is_palindrome = (user_input == user_input[::-1])
    result_message = "Es un palíndromo" if is_palindrome else "No es un palíndromo"
    messagebox.showinfo("Verificación de Palíndromo", result_message)
#Punto 5, transforma cadenas con base en reglas
def transform_string():
    user_input = entry_transform.get()
    transformed_string = ''.join(
        alphabet[(alphabet.index(char) + 1) % len(alphabet)]
        if char in alphabet else char for char in user_input
    )[::-1]
    messagebox.showinfo("Cadena Transformada", f"Cadena transformada: {transformed_string}")

# Función que muestra el menú de operaciones
def show_menu():
    menu_window = tk.Toplevel(root)
    menu_window.title("Menú de Operaciones")

    # Botones individuales para cada cosita
    tk.Button(menu_window, text="Unión de Lenguajes", command=union_languages).pack(pady=10)
    tk.Button(menu_window, text="Concatenación de Lenguajes", command=concatenation_languages).pack(pady=10)
    tk.Button(menu_window, text="operación estrella (Lenguaje 1)", command=lambda: kleene_star(languages[0])).pack(pady=10)
    tk.Button(menu_window, text="Generar Palíndromo", command=generate_palindrome).pack(pady=10)
    tk.Label(menu_window, text="Verificar Palíndromo").pack(pady=5)
    global entry_palindrome
    entry_palindrome = tk.Entry(menu_window)
    entry_palindrome.pack(pady=5)
    tk.Button(menu_window, text="Verificar", command=check_palindrome).pack(pady=5)
    
    tk.Label(menu_window, text="Transformar Cadena").pack(pady=5)
    global entry_transform
    entry_transform = tk.Entry(menu_window)
    entry_transform.pack(pady=5)
    tk.Button(menu_window, text="Transformar", command=transform_string).pack(pady=5)

# Interfaz gráfica acá --- Punto 6
root = tk.Tk()
root.title("Definir Alfabeto y Lenguajes")

tk.Label(root, text="Tamaño del Alfabeto:").pack(pady=5)
entry_alphabet_size = tk.Entry(root)
entry_alphabet_size.pack(pady=5)

tk.Label(root, text="Elementos del Alfabeto (escribir separados por comas):").pack(pady=5)
entry_alphabet_elements = tk.Entry(root)
entry_alphabet_elements.pack(pady=5)


tk.Button(root, text="Definir Lenguajes", command=define_alphabet_and_languages).pack(pady=10)

tk.Button(root, text="Abrir Menú de Operaciones", command=show_menu).pack(pady=20)


root.mainloop()
