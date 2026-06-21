# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
from Crypto.Cipher import AES


class UserForm(forms.Form):
    field = forms.CharField(required=False)
class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest19445(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = RequestPayload(field_value).value
    key = b'0123456789abcdef'
    cipher = AES.new(key, AES.MODE_GCM, nonce=b'000000000000')
    ciphertext = cipher.encrypt(str(data).encode())
    return JsonResponse({'length': len(ciphertext)}, status=200)
