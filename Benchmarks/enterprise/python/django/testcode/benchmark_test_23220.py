# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
from django import forms
import os
import ast


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest23220(request):
    field_value = UserForm(request.POST).data.get('field', '')
    try:
        data = str(ast.literal_eval(field_value))
    except (ValueError, SyntaxError):
        data = field_value
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return JsonResponse({'length': len(ciphertext)}, status=200)
