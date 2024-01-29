import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

class WebServerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Website Hosting")
        self.root.geometry("780x520")
        self.root.configure(bg="#333333") 
        
       
        self.canvas = tk.Canvas(self.root, width=780, height=520, bg="#333333", highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        
        self.set_background_image()
        
       
        self.path_frame = tk.Frame(self.canvas, bg="#333333")
        self.path_frame.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.1)
        
        self.path_label = tk.Label(self.path_frame, text="Pfad:", font=("Arial", 16), bg="#333333", fg="#CCCCCC")
        self.path_label.pack(side=tk.LEFT, padx=5, pady=5)
        
        self.path_entry = tk.Entry(self.path_frame, font=("Arial", 14))
        self.path_entry.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.BOTH, expand=True)
        
        self.browse_button = tk.Button(self.path_frame, text="Durchsuchen", command=self.browse_path, font=("Arial", 14))
        self.browse_button.pack(side=tk.LEFT, padx=5, pady=5)
        
     
        self.port_frame = tk.Frame(self.canvas, bg="#333333")
        self.port_frame.place(relx=0.1, rely=0.35, relwidth=0.8, relheight=0.1)
        
        self.port_label = tk.Label(self.port_frame, text="Port:", font=("Arial", 16), bg="#333333", fg="#CCCCCC")
        self.port_label.pack(side=tk.LEFT, padx=5, pady=5)
        
        self.port_entry = tk.Entry(self.port_frame, font=("Arial", 14))
        self.port_entry.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.BOTH, expand=True)
        
        
        self.button_frame = tk.Frame(self.canvas, bg="#333333")
        self.button_frame.place(relx=0.1, rely=0.5, relwidth=0.8, relheight=0.1)
        
        self.start_button = tk.Button(self.button_frame, text="Starten", command=self.start_server, font=("Arial", 14))
        self.start_button.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.BOTH, expand=True)
        
        self.stop_button = tk.Button(self.button_frame, text="Beenden", command=self.stop_server, font=("Arial", 14))
        self.stop_button.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.BOTH, expand=True)
        
        self.help_button = tk.Button(self.button_frame, text="Hilfe", command=self.show_help, font=("Arial", 14))
        self.help_button.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.BOTH, expand=True)
        
        self.ngrok_button = tk.Button(self.button_frame, text="Mit Ngrok Durchreichen", command=self.start_ngrok, font=("Arial", 14))
        self.ngrok_button.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.BOTH, expand=True)

    def set_background_image(self):
        
        script_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(script_dir, "picture.jpg")
        
       
        if os.path.exists(image_path):
           
            self.background_image = Image.open(image_path)
            self.background_photo = ImageTk.PhotoImage(self.background_image)
            self.canvas.create_image(0, 0, anchor="nw", image=self.background_photo)
        else:
            messagebox.showerror("Fehler", "Das Hintergrundbild wurde nicht gefunden.")
        
    def browse_path(self):
        path = filedialog.askdirectory()
        self.path_entry.delete(0, tk.END)
        self.path_entry.insert(0, path)
        
    def start_server(self):
        path = self.path_entry.get()
        port = self.port_entry.get()
        if not path or not port:
            messagebox.showerror("Fehler", "Bitte Pfad und Port angeben.")
            return
        try:
            port = int(port)
            command = ["python", "-m", "http.server", str(port)]
            subprocess.Popen(command, cwd=path, creationflags=subprocess.CREATE_NEW_CONSOLE)
            messagebox.showinfo("Info", f"Server gestartet auf Port {port}.")
        except Exception as e:
            messagebox.showerror("Fehler", f"Fehler beim Starten des Servers: {e}")
            
    def stop_server(self):
        try:
            subprocess.run(["taskkill", "/f", "/im", "python.exe"], check=True)
            messagebox.showinfo("Info", "Server gestoppt.")
        except Exception as e:
            messagebox.showerror("Fehler", f"Fehler beim Beenden des Servers: {e}")
    
    def start_ngrok(self):
        path = self.path_entry.get()
        port = self.port_entry.get()
        if not path or not port:
            messagebox.showerror("Fehler", "Bitte Pfad und Port angeben.")
            return
        try:
            port = int(port)
            ngrok_path = r"C:\Users\Andreas\OneDrive\Desktop\ngrok-v3-stable-windows-amd64\ngrok"
            command = [ngrok_path, "http", str(port)]
            subprocess.Popen(command, creationflags=subprocess.CREATE_NEW_CONSOLE)
        except Exception as e:
            messagebox.showerror("Fehler", f"Fehler beim Starten von Ngrok: {e}")
            
    def show_help(self):
        help_text = """
        Verwendung:
        1. Wähle einen Pfad zur Website-Ressource.
        2. Gib einen Port ein.
        3. Klicke auf 'Starten', um den Server zu starten.
        4. Klicke auf 'Beenden', um den Server zu stoppen.
        5. Klicke auf 'Mit Ngrok Durchreichen', um Ngrok zu starten.
        
        Hinweis: Stelle sicher, dass Python installiert ist, um den Server zu starten.
        """
        messagebox.showinfo("Hilfe", help_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = WebServerApp(root)
    root.mainloop()
