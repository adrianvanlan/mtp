from django.shortcuts import render, redirect, render_to_response
from django.http import request
from django.contrib.auth import authenticate, login
from django.db.models import Sum
from .models import Nodo, Arco
from .dijkstra import *



def nodos(request):

    nodos = Nodo.objects.all()
    arcos = Arco.objects.all()
    

    if request.method == 'GET':
        coords = ""
            
    elif request.method == 'POST':
        desde = request.POST.get("desde")
        hasta = request.POST.get("hasta")
        variable = request.POST.get("variable")

        G = Graph()
        for nodo in nodos:
            G.add_vertex(nodo.id)
        for arco in arcos:
            if variable=="tiempo":
                G.add_edge(arco.nodo_desde.id, arco.nodo_hasta.id, arco.tiempo)
            else:
                G.add_edge(arco.nodo_desde.id, arco.nodo_hasta.id, arco.costo)
        ids_nodos_bien = shortest_path(G, int(desde), int(hasta))
        nodos_bien = Nodo.objects.filter(id__in=ids_nodos_bien)
        coords = []
        nnn = list(i for i in nodos_bien)
        nnn.sort(key=lambda x: ids_nodos_bien.index(x.id))
        print(G.weights)

        for idx, n in enumerate(nnn[:len(nnn) - 1]):
            c = {"desde": n, "hasta": nnn[idx + 1]}
            coords.append(c)
    

    return render(
        request,
        "mapa.html",
        {
            "nodos": coords,
            "nodos_todos": nodos
        }
    )
