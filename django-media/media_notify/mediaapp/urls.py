from django.urls import path
from .views import media_detail,approve_document,reject_document,form_view

urlpatterns = [
    path('<int:detail_id>/detail',media_detail,name="media_detail"),
    path('approve/<int:doc_id>/',approve_document,name='approve_document'),
    path('reject/<int:doc_id>/',reject_document,name='reject_document'),
    path('<int:detail_id>/form',form_view,name='form_view'),
]
