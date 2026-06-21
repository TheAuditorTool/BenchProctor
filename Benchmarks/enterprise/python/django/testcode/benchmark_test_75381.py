# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
from django import forms
import os


class UserForm(forms.Form):
    field = forms.CharField(required=False)
class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest75381(request):
    field_value = UserForm(request.POST).data.get('field', '')
    ctx = RequestContext(field_value)
    data = ctx.payload
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return JsonResponse({'length': len(ciphertext)}, status=200)
