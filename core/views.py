from django.shortcuts import render, redirect, render_to_response
from django.http import request
from django.contrib.auth import authenticate, login
from .models import Nodo, Arco
from .dijkstra import *


def nodos(request):
    nodos = Nodo.objects.all()
    G = Graph()
    for nodo in nodos:
        G.add_vertex(nodo.id)
    arcos = Arco.objects.all()
    for arco in arcos:
        G.add_edge(arco.nodo_desde.id, arco.nodo_hasta.id, arco.tiempo)
    ids_nodos_bien = shortest_path(G, 1, 7)
    nodos_bien = Nodo.objects.filter(id__in=ids_nodos_bien)

    print(nodos_bien)
    coords = []
    nnn = list(i for i in nodos_bien)
    nnn.sort(key=lambda x: ids_nodos_bien.index(x.id))
    print("Bien: ", nnn)

    for idx, n in enumerate(nnn[:len(nnn)-1]):
        c = {"desde": n, "hasta": nnn[idx+1]}
        coords.append(c)

    return render_to_response(
        "mapa.html",
        {"nodos": coords}
    )
