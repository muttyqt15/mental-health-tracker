from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306207101',
        'name': 'Muttaqin Muzakkir',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)