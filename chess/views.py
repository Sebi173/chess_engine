# Create your views here.

from django.shortcuts import render
from .magic.calculate_coordinates import calculate_coordinates_for_all_pieces
from .magic.load_starting_position import load_starting_position
from .magic.calculate_legal_moves import calculate_legal_moves

def index(request):
    if request.method == "POST":
        listPosition = load_starting_position()
        dicCoordinates = calculate_coordinates_for_all_pieces(listPosition)
        chessPiece = request.POST.get("id", "")
        dicCoordinates = calculate_legal_moves(chessPiece, dicCoordinates)
        return render(request, "index.html", dicCoordinates)
    
    listPosition = load_starting_position()
    dicCoordinates = calculate_coordinates_for_all_pieces(listPosition)

    return render(request, "index.html", dicCoordinates)