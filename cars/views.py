#from django.http import HttpResponse
from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import CarModelForm


# Create your views here.
def cars_view(resquest):
    cars = Car.objects.all()  # Get all cars
    search = resquest.GET.get('search', None)
    
    if search:
        cars = Car.objects.filter(model__contains=search)  # Filter cars by model name
    # This line is just to ensure the model is loaded, not necessary for the view.

    return render(
        resquest,
        'cars.html',
        {'cars': cars}
    )


def new_car_view(request):
    if request.method == 'POST':
        new_car_form = CarModelForm(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('cars_list') 
    else:
        #new_car_form = CarForm()
        new_car_form = CarModelForm()
    return render(request, 'new_car.html', {'new_car_form': new_car_form})