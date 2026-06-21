# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
from Crypto.Cipher import DES


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest50663(request):
    field_value = UserForm(request.POST).data.get('field', '')
    parts = []
    for token in str(field_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    ciphertext = DES.new(b'8bytekey', DES.MODE_ECB).encrypt(str(data).encode().ljust(8)[:8])
    return JsonResponse({'length': len(ciphertext)}, status=200)
