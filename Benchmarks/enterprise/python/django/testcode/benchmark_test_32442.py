# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
from Crypto.Cipher import DES


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest32442(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = (lambda v: v.strip())(field_value)
    ciphertext = DES.new(b'8bytekey', DES.MODE_ECB).encrypt(str(data).encode().ljust(8)[:8])
    return JsonResponse({'length': len(ciphertext)}, status=200)
