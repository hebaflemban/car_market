from django.shortcuts import render, redirect
from .models import Car
from .forms import CarForm
from django.contrib import messages

def home(request):
	context = {
		'msg' : 'We got awesome cars'
	}

	return render(request, 'home.html', context)

def msg(request):
	context = {
		'msg' : 'We got awesome cars'
	}


	return render(request, 'confirmationMsg.html', context)


def car_list(request):
	cars = Car.objects.all()
	context = {
		"cars": cars,
	}
	return render(request, 'car_list.html', context)


def car_detail(request, car_id):
	car = Car.objects.get(id=car_id)
	context = {
		"car": car,
	}
	return render(request, 'car_detail.html', context)


def car_create(request):
	car_form = CarForm()
	if request.method == 'POST':
		car_form = CarForm(request.POST, request.FILES)
		if car_form.is_valid():
			car_form.save()
			messages.success(request, 'Car added successfully')
			return redirect ('confirmation')
	context = {
		'form' : car_form
	}
	return render(request, 'car-create.html', context)


def car_update(request, car_id):
	car_obj = Car.objects.get(id=car_id)
	car_form = CarForm(instance = car_obj)
	if request.method == 'POST':
		car_form = CarForm(request.POST, request.FILES, instance = car_obj)
		if car_form.is_valid():
			car_form.save()
			messages.success(request, 'Car updated successfully')
			return redirect ('confirmation')

	context = {
		'form' : car_form,
		'car_obj' : car_obj
	}

	return render(request, 'car-update.html', context)


def car_delete(request, car_id):
	car_obj = Car.objects.get(id = car_id)
	car_obj.delete()
	messages.success(request, 'Car removed from list')
	return redirect ('confirmation')
