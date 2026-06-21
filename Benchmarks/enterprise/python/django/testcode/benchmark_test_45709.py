# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
from urllib.parse import unquote
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest45709(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = unquote(field_value)
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
