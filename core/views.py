from django.shortcuts import render, redirect, render_to_response
from django.http import request
from django.contrib.auth import authenticate, login
from .models import Nodo, Arco
from .dijkstra import *

def index(request):
    return render_to_response("index.html", {})

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        render_to_response("index.html", {})
    else:
        render_to_response("index.html", {})
        # Return an 'invalid login' error message.

def logout_view(request):
    logout(request)

def nodos(request):
    nodos = Nodo.objects.all()
    G = Graph()
    for nodo in nodos:
        G.add_vertex(nodo.id)
    arcos = Arco.objects.all()
    for arco in arcos:
        G.add_edge(arco.nodo_desde.id, arco.nodo_hasta.id, arco.tiempo)
    ids_nodos_bien = shortest_path(G, 1, 7)
    print(ids_nodos_bien)
    nodos_bien = Nodo.objects.filter(id__in=ids_nodos_bien).order_by('-id')
    print(nodos_bien)
    d = dict((i,None) for i in ids_nodos_bien)
    for n in nodos_bien:
        d[n.id] = n
    print(d)
    desde = nodos_bien[0]
    hasta = nodos_bien[len(nodos_bien)-1]
    nodos_bien.exclude(id=desde.id)
    nodos_bien.exclude(id=hasta.id)
    return render_to_response(
        "nodos.html",
        {"nodos": nodos_bien, "desde": desde, "hasta": hasta, "waypts": nodos_bien}
    )
