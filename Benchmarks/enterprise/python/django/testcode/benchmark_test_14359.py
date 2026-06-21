# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import os
from django import forms
import time


class UserForm(forms.Form):
    field = forms.CharField(required=False)
def coalesce_blank(value):
    return value or ''

def BenchmarkTest14359(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = coalesce_blank(field_value)
    store_cred = os.environ.get('APP_SECRET', '')
    key_expires_at = 4102444800
    active_key = store_cred if key_expires_at > int(time.time()) else os.environ['DATA_ENC_KEY_CURRENT']
    Fernet(active_key.encode()).encrypt(str(data).encode())
    return JsonResponse({"saved": True})
