# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
import json
from Crypto.Cipher import AES


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest55626(request):
    field_value = UserForm(request.POST).data.get('field', '')
    try:
        data = json.loads(field_value).get('value', field_value)
    except (json.JSONDecodeError, AttributeError):
        data = field_value
    key = b'0123456789abcdef'
    cipher = AES.new(key, AES.MODE_GCM, nonce=b'000000000000')
    ciphertext = cipher.encrypt(str(data).encode())
    return JsonResponse({'length': len(ciphertext)}, status=200)
