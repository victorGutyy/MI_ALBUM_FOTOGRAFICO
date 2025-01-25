import tkinter as tk

def open_section(section_name):
    # Crear una nueva ventana para la sección
    section_window = tk.Toplevel()
    section_window.title(section_name)
    section_window.geometry("800x600")

    # Mostrar el nombre de la sección
    label = tk.Label(section_window, text=f"Sección: {section_name}", font=("Arial", 16))
    label.pack(pady=20)

    # Botón para cerrar la ventana de la sección
    close_button = tk.Button(section_window, text="Cerrar", command=section_window.destroy)
    close_button.pack(pady=20)

def main():
    # Crear la ventana principal
    root = tk.Tk()
    root.title("MI ÁLBUM FOTOGRÁFICO")
    root.geometry("800x600")  # Tamaño de la ventana

    # Etiqueta de bienvenida
    label = tk.Label(root, text="¡Bienvenido a MI ÁLBUM FOTOGRÁFICO!", font=("Arial", 16))
    label.pack(pady=20)

    # Botones para cada sección
    sections = ["Mamá", "Papá", "Hermanos", "Familia", "Amigos", "Trabajo"]
    for section in sections:
        button = tk.Button(root, text=section, command=lambda sec=section: open_section(sec))
        button.pack(pady=5)

    # Botón de salida
    exit_button = tk.Button(root, text="Salir", command=root.quit)
    exit_button.pack(pady=20)

    # Ejecutar la aplicación
    root.mainloop()

if __name__ == "__main__":
    main()
