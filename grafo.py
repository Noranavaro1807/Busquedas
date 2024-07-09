
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import networkx as nx

# Función para visualizar el grafo
def visualizar_grafo(camino_numeros=None):
    # Crear un grafo vacío
    G = nx.Graph()

    # Agregar nodos al grafo
    for i in range(27):
        G.add_node(i)

    # Agregar aristas al grafo
    G.add_edges_from([(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (2, 5), (3, 4), (4, 6), (4, 5), 
                    (5, 8), (5, 6), (6, 7), (6, 8), (7, 10), (7, 11), (8, 11), (8, 9), 
                    (9, 11), (9, 16), (10, 11), (10, 12), (11, 12), (11, 14), (12, 13), 
                    (13, 15), (13, 21), (14, 16), (14, 15), (14, 17), (15, 21), (16, 18), 
                    (16, 19), (17, 18), (17, 21), (18, 21), (18, 20), (18, 19), (19, 22), 
                    (20, 23), (21, 23), (21, 25), (22, 23), (22, 24), (23, 24), (23, 25), 
                    (24, 25), (24, 26), (25, 26)])

    # Definir las posiciones de los nodos manualmente
    posiciones_personalizadas = {
        0: (10, 0.63), 1: (9.2, 0.78), 2: (8.7, 0.50), 3: (8.5, 0.80), 4: (7.8, 0.82),
        5: (7.50, 0.50), 6: (7.252, 0.71), 7: (6.5, 0.80), 8: (6.45, 0.49), 9: (5.65, 0.45),
        10: (5.75, 0.89), 11: (5.50, 0.65), 12: (5.1, 0.80), 13: (4.3, 0.82), 14: (4.2, 0.50),
        15: (3.90, 0.65), 16: (4.0, 0.40), 17: (2.80, 0.60), 18: (2.0, 0.55), 19: (1.8, 0.45),
        20: (1.3, 0.55), 21: (1.6, 0.65), 22: (1, 0.47), 23: (0, 0.60), 24: (-1.5, 0.47),
        25: (0, 0.70), 26: (-1, 0.80),
    }

    # Crear un diccionario para mapear los nombres de los nodos
    nombres_nodos = {
        0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j',
        10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'ñ', 15: 'o', 16: 'p', 17: 'q', 18: 'r',
        19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'
    }
    nodos_nombres = {v: k for k, v in nombres_nodos.items()}

    # Ajustar el tamaño de la figura
    #
    fig.clear()
    ax = fig.add_subplot(111)
    
    if camino_numeros:
        # Verificar si el camino elegido es válido
        camino_valido = True
        for i in range(len(camino_numeros) - 1):
            if not G.has_edge(camino_numeros[i], camino_numeros[i + 1]):
                camino_valido = False
                break
        

        if camino_valido:
            mensaje_estado.config(text=f"El camino ingresado es válido.")
            # Función para visualizar el camino y resaltar las aristas en rojo
            path_edges = list(zip(camino_numeros, camino_numeros[1:]))
            nx.draw(G, pos=posiciones_personalizadas, labels=nombres_nodos, with_labels=True, node_color='skyblue', ax=ax)
            nx.draw_networkx_nodes(G, pos=posiciones_personalizadas, nodelist=camino_numeros, node_color='r', ax=ax)
            nx.draw_networkx_edges(G, pos=posiciones_personalizadas, edgelist=path_edges, edge_color='r', width=2, ax=ax)
        else:
            mensaje_estado.config(text="El camino ingresado no es válido.")
            nx.draw(G, pos=posiciones_personalizadas, labels=nombres_nodos, with_labels=True, node_color='skyblue', ax=ax)
    else:
        # Visualizar el grafo sin rutas al inicio
        nx.draw(G, pos=posiciones_personalizadas, labels=nombres_nodos, with_labels=True, node_color='skyblue', ax=ax)
    
    canvas.draw()

# Crear una aplicación de Tkinter
app = tk.Tk()
app.title("BUSQUEDAS")
app.geometry('1400x420')
app.configure(background='black')

# Crear un contenedor para la interfaz de usuario
frame_interfaz = ttk.Frame(app)
frame_interfaz.pack(side=tk.LEFT, padx=10, pady=10)

# Instrucciones
instrucciones_texto = "Ingrese los nombres de los nodos del camino separados por comas (por ejemplo, a,b,d,e):"
instrucciones = ttk.Label(frame_interfaz, text=instrucciones_texto, font=("Arial", 10, "bold"))
instrucciones.grid(row=0, column=0, columnspan=2, pady=5)

# Entrada de texto para ingresar el camino
entrada_camino = ttk.Entry(frame_interfaz, width=50)
entrada_camino.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

# Botón para iniciar la búsqueda y visualización
def buscar_y_visualizar():
    camino_nombres = entrada_camino.get().split(',')
    nodos_nombres = {
        0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j',
        10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'ñ', 15: 'o', 16: 'p', 17: 'q', 18: 'r',
        19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'
    }
    nodos_nombres = {v: k for k, v in nodos_nombres.items()}
    camino_numeros = [nodos_nombres[nodo_nombre] for nodo_nombre in camino_nombres]
    visualizar_grafo(camino_numeros)
    
#botones

boton_Aserch = ttk.Button(frame_interfaz, text="A search", command=buscar_y_visualizar)
boton_Aserch.grid(row=2, column=0, columnspan=2, padx=7, pady=10)
boton_Aserch.config(width=20)

boton_best= ttk.Button(frame_interfaz, text=f"Best First ", command=buscar_y_visualizar)
boton_best.grid(row=3, column=0, columnspan=2, padx=7, pady=10)
boton_best.config(width=20)

boton_hill= ttk.Button(frame_interfaz, text=f"Hill Climbing ", command=buscar_y_visualizar)
boton_hill.grid(row=4, column=0, columnspan=2, padx=7, pady=10)
boton_hill.config(width=20)
    
boton_dij= ttk.Button(frame_interfaz, text=f"Dijkstra ", command=buscar_y_visualizar)
boton_dij.grid(row=5, column=0, columnspan=2, padx=7, pady=10)
boton_dij.config(width=20)
    

# Etiqueta para mostrar el estado del camino
mensaje_estado = ttk.Label(frame_interfaz, text="")
mensaje_estado.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

# Crear un contenedor 
frame_grafo = ttk.Frame(app)
frame_grafo.pack(side=tk.RIGHT, padx=15, pady=10)

# Crear la figura 
fig, ax = plt.subplots(figsize=(15, 6))  # Ajustar el tamaño de la figura aquí
canvas = FigureCanvasTkAgg(fig, master=frame_grafo)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Visualizar el grafo inicial
visualizar_grafo()

# Ejecutar la aplicación
app.mainloop()
