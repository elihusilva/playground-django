from django.urls import path
from .views import PageListView, PageDetailView, PageCreate, PageUpdate, PageDelete

# urlpatterns = [
#     path('<slug:page_slug>/', views.page, name='page'),
# ]

pages_patterns = ([
    path('pages', PageListView.as_view(), name='pages'),
    path('page/<slug:slug>', PageDetailView.as_view(), name='page'),
    path('page/create/', PageCreate.as_view(), name='create'),
    path('page/update/<int:pk>/', PageUpdate.as_view(), name='update'),
    path('page/delete/<int:pk>/', PageDelete.as_view(), name='delete')
], 'pages')