from django.urls import path
from money_tracker.views import *

app_name = 'money_tracker'

urlpatterns = [
    path('', show_tracker, name='show_tracker'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'),
    path('create/', create_transaction, name='create_transaction'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('modify/<int:id>', modify_transaction, name='modify_transaction'),
    path('delete/<int:id>', delete_transaction, name='delete_transaction'),
    path('create-ajax/', create_transaction_ajax, name='create_transaction_ajax'),
    path('create-flutter/', create_transaction_flutter, name='create_transaction_flutter'),
]
