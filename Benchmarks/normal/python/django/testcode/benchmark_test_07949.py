# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
import asyncio
from Crypto.Cipher import AES


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest07949(request):
    field_value = UserForm(request.POST).data.get('field', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return field_value
    data = asyncio.run(fetch_payload())
    key = b'0123456789abcdef'
    cipher = AES.new(key, AES.MODE_GCM, nonce=b'000000000000')
    ciphertext = cipher.encrypt(str(data).encode())
    return JsonResponse({'length': len(ciphertext)}, status=200)
