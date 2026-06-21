# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
from django import forms
import os


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest75251(request):
    field_value = UserForm(request.POST).data.get('field', '')
    key = os.environ['DATA_ENC_KEY'].encode()
    encrypted = Fernet(key).encrypt(str(field_value).encode())
    with open('/var/data/secrets.enc', 'wb') as fh:
        fh.write(encrypted)
    return JsonResponse({"saved": True})
