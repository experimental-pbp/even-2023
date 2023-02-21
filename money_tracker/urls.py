from django.urls import path
from money_tracker.views import show_tracker, show_xml, show_json, show_json_by_id, create_transaction

app_name = 'money_tracker'

urlpatterns = [
    path('', show_tracker, name='show_tracker'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'),
    path('create', create_transaction, name='create_transaction'),
]
