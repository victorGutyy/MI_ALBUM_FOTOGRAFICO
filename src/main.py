import tkinter as tk

def main():
    # Crear la ventana principal
    root = tk.Tk()
    root.title("MI ÁLBUM FOTOGRÁFICO")
    root.geometry("800x600")  # Tamaño de la ventana

    # Etiqueta de bienvenida
    label = tk.Label(root, text="¡Bienvenido a MI ÁLBUM FOTOGRÁFICO!", font=("Arial", 16))
    label.pack(pady=20)

    # Botón de salida
    exit_button = tk.Button(root, text="Salir", command=root.quit)
    exit_button.pack(pady=20)

    # Ejecutar la aplicación
    root.mainloop()

if __name__ == "__main__":
    main()
