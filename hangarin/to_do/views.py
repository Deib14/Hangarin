from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from to_do.models import Task, Category, Priority, Note, SubTask
from to_do.forms import TaskForm, CategoryForm, SubTaskForm, PriorityForm, NoteForm
from django.urls import reverse_lazy
from django.db.models import Q
from django.utils import timezone

class HomePageView(ListView):
    model = Task
    context_object_name = 'home'
    template_name = "home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_task"] = Task.objects.count()
        context["total_subtask"] = SubTask.objects.count()
        context["total_note"] = Note.objects.count()
        today = timezone.now().date()
        context["task_due_today"] = Task.objects.filter(deadline__date=today).count()
        return context
    
class TaskList(ListView):
    model = Task
    context_object_name = 'task'
    template_name = 'task_list.html'
    paginate_by = 5
    
    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')

        if query:
            qs = qs.filter(
                Q(title__icontains=query) |
                Q(category__name__icontains=query)
                )
        return qs
    
    def get_ordering(self):
        allowed = ["title", "category__name", "priority__name", "status", "deadline", "-deadline"]
        sort_by = self.request.GET.get("sort_by")
        if sort_by in allowed:
            return sort_by
        return "title" # make the return the last selected sort option?
    
class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('task-list')
    
class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('task-list')
    
class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task_del.html'
    success_url = reverse_lazy('task-list')

class SubTaskList(ListView):
    model = SubTask
    context_object_name = 'subtask'
    template_name = 'subtask_list.html'
    paginate_by = 5
    
    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')

        if query:
            qs = qs.filter(
                Q(title__icontains=query) |
                Q(status__icontains=query) |
                Q(task__title__icontains=query)
                )
        return qs
    
    def get_ordering(self):
        allowed = ["title", "status", "task__title"]
        sort_by = self.request.GET.get("sort_by")
        if sort_by in allowed:
            return sort_by
        return "title" 
    
    
class SubTaskCreateView(CreateView):
    model = SubTask
    form_class = SubTaskForm
    template_name = 'subtask_form.html'
    success_url = reverse_lazy('subtask-list')
    
class SubTaskUpdateView(UpdateView):
    model = Category
    form_class = SubTaskForm
    template_name = 'subtask_form.html'
    success_url = reverse_lazy('subtask-list')
    
class SubTaskDeleteView(DeleteView):
    model = SubTask
    template_name = 'subtask_del.html'
    success_url = reverse_lazy('subtask-list')
    
class CategoryList(ListView):
    model = Category
    context_object_name = 'category'
    template_name = 'category_list.html'
    paginate_by = 5
    
    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')

        if query:
            qs = qs.filter(
                Q(name__icontains=query)
                )
        return qs
    
    def get_ordering(self):
        allowed = ["name"]
        sort_by = self.request.GET.get("sort_by")
        if sort_by in allowed:
            return sort_by
        return "name" 

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_form.html'
    success_url = reverse_lazy('category-list')
    
class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_form.html'
    success_url = reverse_lazy('category-list')
    
class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'category_del.html'
    success_url = reverse_lazy('category-list')
    

    
class PriorityList(ListView):
    model = Priority
    context_object_name = 'subtask'
    template_name = 'priority_list.html'
    paginate_by = 5
    
    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')

        if query:
            qs = qs.filter(
                Q(name__icontains=query)
                )
        return qs
    
    def get_ordering(self):
        allowed = ["name"]
        sort_by = self.request.GET.get("sort_by")
        if sort_by in allowed:
            return sort_by
        return "name" 
    
class PriorityCreateView(CreateView):
    model = Priority
    form_class = PriorityForm
    template_name = 'priority_form.html'
    success_url = reverse_lazy('priority-list')
    
class PriorityUpdateView(UpdateView):
    model = Priority
    form_class = PriorityForm
    template_name = 'priority_form.html'
    success_url = reverse_lazy('priority-list')
    
class PriorityDeleteView(DeleteView):
    model = Priority
    template_name = 'priority_del.html'
    success_url = reverse_lazy('priority-list')
    
class NoteList(ListView):
    model = Note
    context_object_name = 'note'
    template_name = 'note_list.html'
    paginate_by = 5
    
    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')

        if query:
            qs = qs.filter(
                Q(task__title__icontains=query) |
                Q(content__icontains=query)
                )
        return qs
    
    def get_ordering(self):
        allowed = ["task__title", "content", "created_at"]
        sort_by = self.request.GET.get("sort_by")
        if sort_by in allowed:
            return sort_by
        return "task__title"
    
class NoteCreateView(CreateView):
    model = Note
    form_class = NoteForm
    template_name = 'note_form.html'
    success_url = reverse_lazy('note-list')
    
class NoteUpdateView(UpdateView):
    model = Note
    form_class = NoteForm
    template_name = 'note_form.html'
    success_url = reverse_lazy('note-list')
    
class NoteDeleteView(DeleteView):
    model = Note
    template_name = 'note_del.html'
    success_url = reverse_lazy('note-list')
    
