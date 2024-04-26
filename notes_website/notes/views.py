from django.shortcuts import render, redirect
from django.contrib import messages

from .Form import NotesForm

from .models import Notes


def index(request):

	item_list = Notes.objects.order_by("date")
	if request.method == "POST":
		note = NotesForm(request.POST)
		if note.is_valid():
			note.save()
			return redirect('notes')
	form = NotesForm()

	page = {
		"forms": form,
		"list": item_list,
		"title": "Notes LIST",
	}
	return render(request, 'index.html', page)


def remove(request, item_id):
	item = Notes.objects.get(id=item_id)
	item.delete()
	messages.info(request, "item removed !!!")
	return redirect('notes')
