# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
from urllib.parse import unquote
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest13914(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = unquote(field_value)
    digest = str(data).encode().hex()
    return JsonResponse({'digest': str(digest)}, status=200)
