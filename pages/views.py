from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
from .forms import CommentForm



# Vistas estáticas (si las necesitas)
def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')


# Listado de posts
class PostListView(ListView):
    model = Post
    template_name = 'pages/pages_list.html'
    context_object_name = 'posts'
    ordering = ['-fecha']


# Detalle de post + formulario de comentarios
class PostDetailView(FormMixin, DetailView):
    model = Post
    template_name = 'pages/post_detail.html'
    context_object_name = 'post'
    form_class = CommentForm

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post   = self.object
            comment.author = request.user
            comment.save()
            return self.form_valid(form)
        return self.form_invalid(form)

    def get_success_url(self):
        return self.request.path
