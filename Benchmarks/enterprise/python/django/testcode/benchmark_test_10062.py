# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
from django import forms
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest10062(request):
    field_value = UserForm(request.POST).data.get('field', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(field_value)
    data = collected
    if not re.match(r'^.{1,256}$', str(data)):
        return JsonResponse({'error': 'schema invalid'}, status=400)
    key = RSA.generate(512)
    ciphertext = PKCS1_OAEP.new(key).encrypt(str(data).encode()[:22])
    return JsonResponse({'length': len(ciphertext)}, status=200)
