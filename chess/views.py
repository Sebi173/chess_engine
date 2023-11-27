# Create your views here.

from django.shortcuts import render
from .magic.calculate_coordinates import calculate_coordinates_for_all_pieces
from .magic.load_starting_position import load_starting_position

def index(request):
    listPosition = load_starting_position()

    dicCoordinates = calculate_coordinates_for_all_pieces(listPosition)

    return render(request, "index.html", dicCoordinates)