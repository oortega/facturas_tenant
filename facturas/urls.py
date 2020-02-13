from django.conf.urls import url
from django.views.generic import RedirectView
from django.urls import path, include
from django.urls import reverse_lazy

from .views import *

urlpatterns = [
    url(r'^$', factura_empresa, name="factura_empresa"),
    path('chat/', BroadcastChatView.as_view(), name='broadcast_chat'),
    path('userchat/', UserChatView.as_view(), name='user_chat'),
    path('groupchat/', GroupChatView.as_view(), name='group_chat'),
    path('accounts/', include('django.contrib.auth.urls')),
    
    path('', RedirectView.as_view(url=reverse_lazy('broadcast_chat'))),
]