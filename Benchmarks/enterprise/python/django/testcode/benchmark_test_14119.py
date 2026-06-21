# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest14119(request):
    field_value = UserForm(request.POST).data.get('field', '')
    ciphertext = bytes(b ^ 0x42 for b in str(field_value).encode())
    return JsonResponse({'length': len(ciphertext)}, status=200)
