import tkinter as tk
from PIL import Image, ImageTk
import time
root=tk.Tk()
root.title("tamagochiii")

ruta_normal=r"C:\Users\Solange\Desktop\lolaaa\tamagochi_second_try\fotos_tamagochi\fondo con perro normal.png"
ruta_juego=r"C:\Users\Solange\Desktop\lolaaa\tamagochi_second_try\fotos_tamagochi\fondo perro juego.png"
ruta_baño=r"C:\Users\Solange\Desktop\lolaaa\tamagochi_second_try\fotos_tamagochi\fondo perro baño.png"
ruta_comida=r"C:\Users\Solange\Desktop\lolaaa\tamagochi_second_try\fotos_tamagochi\fondo perro comida.png"
ruta_mimos=r"C:\Users\Solange\Desktop\lolaaa\tamagochi_second_try\fotos_tamagochi\fondo perro mimos.png"

imagen_normal = Image.open(ruta_normal)
perro_normal = ImageTk.PhotoImage(imagen_normal)

fondo = tk.Label(root, image=perro_normal)
fondo.place(x=0, y=0, relwidth=1, relheight=1)

imagen_comer=Image.open(ruta_comida)
fondo_comer=ImageTk.PhotoImage(imagen_comer)

imagen_jugar=Image.open(ruta_juego)
fondo_jugar=ImageTk.PhotoImage(imagen_jugar)

imagen_bañar=Image.open(ruta_baño)
fondo_bañar=ImageTk.PhotoImage(imagen_bañar)

imagen_mimar=Image.open(ruta_mimos)
fondo_mimar=ImageTk.PhotoImage(imagen_mimar)

class mascota_virtual():
    def __init__(self, nombre, hambre, aburrimiento, cariño, higiene):
        self.name=nombre
        self.hambre=hambre
        self.aburrimiento=aburrimiento
        self.cariño=cariño
        self.higiene=higiene


    def comer(self):
        self.hambre+=5
        if self.hambre==100:
            self.hambre=self.hambre


        fondo.config(image=fondo_comer)
        root.after(2000, lambda: fondo.config(image=perro_normal))

    def jugar (self):
        self.aburrimiento-=5
        if self.aburrimiento==0:
           self.aburrimiento=self.aburrimiento

        fondo.config(image=fondo_jugar)
        root.after(2000, lambda: fondo.config(image=perro_normal))


    def mimar(self):
        self.cariño+=5
        if self.cariño==100:
            self.cariño=self.cariño

        fondo.config(image=fondo_mimar)
        root.after(2000, lambda: fondo.config(image=perro_normal))

       
    def bañar(self):
        self.higiene+=5
        if self.higiene==100:
            self.higiene=self.higiene
    
        fondo.config(image=fondo_bañar)
        root.after(2000, lambda: fondo.config(image=perro_normal))

    

    def disminuir_salud_periodicamente(self, intervalo_segundos=10, decrecimiento=10):
        tiempo_actual = time.time()
        tiempo_transcurrido = tiempo_actual - self.tiempo_pasado

        if tiempo_transcurrido >= intervalo_segundos:
            self.higiene-= decrecimiento
            self.aburrimiento+=decrecimiento
            self.hambre+=decrecimiento
            self.cariño-=decrecimiento
            self.tiempo_pasado = tiempo_actual
            
mi_mascota=mascota_virtual("corgie", 100, 0, 100, 100)


label_hambre=tk.Label(root, text="hambre:"+ str(mi_mascota.hambre), font="arial 20",bg="pink")
label_hambre.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W )

label_aburrimiento=tk.Label(root, text="aburrimiento: "+ str(mi_mascota.aburrimiento), font="arial 20", bg="pink")
label_aburrimiento.grid (row=1, column=0, padx=10, pady=10, sticky=tk.W)

label_cariño=tk.Label(root, text="amor:"+ str(mi_mascota.cariño), font="arial 20", bg="pink")
label_cariño.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)

label_higiene=tk.Label(root, text="higiene: "+ str(mi_mascota.higiene), font="arial 20", bg="pink")
label_higiene.grid(row=4, column=0, padx=10, pady=10, sticky=tk.W)


root.grid_rowconfigure(1, weight=0) 
root.grid_columnconfigure(0, weight=0) 

for i in range(5,24):
    espacio=tk.Label(text="")
    espacio.grid(row=i, column=0)

for i in range(1,25):
    espacio2=tk.Label(text="")
    espacio2.grid(row=25, column=i)


boton_comer= tk.Button(root, text="alimentar", command=mi_mascota.comer,bg="#DCB0FF", font="arial 20")
boton_comer.grid(row=25, column=26, padx=20, pady=10, sticky=tk.SE)

boton_jugar= tk.Button(root, text="jugar", command=mi_mascota.jugar,bg="#DCB0FF", font="arial 20" )
boton_jugar.grid(row=25, column=27, padx=20, pady=10, sticky=tk.SE)

boton_mimos= tk.Button(root, text="mimar", command=mi_mascota.mimar, bg="#DCB0FF", font="arial 20")
boton_mimos.grid(row=25, column=28, padx=20, pady=10, sticky=tk.SE)

boton_baño= tk.Button(root, text="bañar", command=mi_mascota.bañar,bg="#DCB0FF", font="arial 20" )
boton_baño.grid(row=25, column=29, padx=20, pady=10, sticky=tk.SE)



root.mainloop()