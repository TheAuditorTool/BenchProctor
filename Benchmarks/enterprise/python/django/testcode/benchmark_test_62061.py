# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest62061(request):
    field_value = UserForm(request.POST).data.get('field', '')
    prefix = ''
    data = prefix + str(field_value)
    key = RSA.generate(512)
    ciphertext = PKCS1_OAEP.new(key).encrypt(str(data).encode()[:22])
    return JsonResponse({'length': len(ciphertext)}, status=200)
