# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
from Crypto.Cipher import AES


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest21860(request):
    field_value = UserForm(request.POST).data.get('field', '')
    pending = list(str(field_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    key = b'0123456789abcdef'
    cipher = AES.new(key, AES.MODE_GCM, nonce=b'000000000000')
    ciphertext = cipher.encrypt(str(data).encode())
    return JsonResponse({'length': len(ciphertext)}, status=200)
