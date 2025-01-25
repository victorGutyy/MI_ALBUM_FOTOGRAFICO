import tkinter as tk

def open_section(section_name):
    # Crear una nueva ventana para la sección
    section_window = tk.Toplevel()
    section_window.title(section_name)
    section_window.geometry("800x600")
    section_window.configure(bg="#f4f4f9")  # Fondo de la ventana

    # Mostrar el nombre de la sección
    label = tk.Label(
        section_window, text=f"Sección: {section_name}",
        font=("Arial", 18), bg="#f4f4f9", fg="#333"
    )
    label.pack(pady=20)

    # Botón para cerrar la ventana de la sección
    close_button = tk.Button(
        section_window, text="Cerrar", command=section_window.destroy,
        bg="#ff6b6b", fg="white", font=("Arial", 12), relief="flat"
    )
    close_button.pack(pady=20)

def main():
    # Crear la ventana principal
    root = tk.Tk()
    root.title("MI ÁLBUM FOTOGRÁFICO")
    root.geometry("800x600")  # Tamaño de la ventana
    root.configure(bg="#f4f4f9")  # Fondo de la ventana principal

    # Etiqueta de bienvenida
    label = tk.Label(
        root, text="¡Bienvenido a MI ÁLBUM FOTOGRÁFICO!",
        font=("Arial", 20, "bold"), bg="#f4f4f9", fg="#4a4a4a"
    )
    label.pack(pady=20)

    # Botones para cada sección
    sections = ["Mamá", "Papá", "Hermanos", "Familia", "Amigos", "Trabajo"]
    for section in sections:
        button = tk.Button(
            root, text=section, command=lambda sec=section: open_section(sec),
            bg="#6c5ce7", fg="white", font=("Arial", 14), width=20, relief="flat"
        )
        button.pack(pady=10)

    # Botón de salida
    exit_button = tk.Button(
        root, text="Salir", command=root.quit,
        bg="#d63031", fg="white", font=("Arial", 14), width=20, relief="flat"
    )
    exit_button.pack(pady=20)

    # Ejecutar la aplicación
    root.mainloop()

if __name__ == "__main__":
    main()
