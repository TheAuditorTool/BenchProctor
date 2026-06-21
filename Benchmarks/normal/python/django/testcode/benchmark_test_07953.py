# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
from django import forms
import os


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest07953(request):
    field_value = UserForm(request.POST).data.get('field', '')
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(field_value).encode())
    return JsonResponse({'length': len(ciphertext)}, status=200)
