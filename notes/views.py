from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Notes
from .forms import NotesForm


class NotesDeleteView(DeleteView):
    '''Deletes a Note'''
    model = Notes
    success_url = '/smart/notes'
    template_name = "notes/notes_delete.html"


class NotesUpdateView(UpdateView):
    '''Updates a Note'''
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm
    template_name = "notes/notes_form.html"


class NotesCreateView(LoginRequiredMixin, CreateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm
    login_url = "/login"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class NotesListView(LoginRequiredMixin, ListView):
    '''List the Notes for logged in user'''
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html"
    login_url = "/login"

    def get_queryset(self):
        return self.request.user.notes.all()


class NotesDetailView(DetailView):
    '''Lists Detailed Note'''
    model = Notes
    context_object_name = "note"
    template_name = "notes/notes_detail.html"
