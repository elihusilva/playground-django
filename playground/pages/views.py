# Librerias CRUD.
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from .models import Page
from .forms import PageForm

# Create your views here.
class PageListView(ListView):
    model = Page
    paginate_by = 2

# def page(request, page_slug):
#     page = get_object_or_404(Page, slug=page_slug)
#     return render(request, 'pages/page.html', {'page':page})

# Mixin que requiere que el usuario sea miembro del Staff.
class StaffRequiredMixin(object):
    
    # Si el usuario está loggeado, le permite crear páginas.
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)
    
class PageDetailView(DetailView):
    model = Page

# Clase para crear nuevas páginas.
@method_decorator(staff_member_required, name='dispatch')
class PageCreate(CreateView):
    model = Page
    form_class = PageForm
    success_url = reverse_lazy('pages:pages')

# Clase para actualizar páginas.
@method_decorator(staff_member_required, name='dispatch')
class PageUpdate(UpdateView):
    model = Page
    form_class = PageForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('pages:update', args=[self.object.id]) + '?success'
    
# Clase para eliminar páginas.
@method_decorator(staff_member_required, name='dispatch')
class PageDelete(DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')