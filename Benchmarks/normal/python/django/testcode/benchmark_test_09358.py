# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import unquote
from django import forms
import tempfile


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest09358(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = unquote(field_value)
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
