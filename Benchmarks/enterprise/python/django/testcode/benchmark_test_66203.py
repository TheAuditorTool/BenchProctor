# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
import tempfile


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest66203(request):
    field_value = UserForm(request.POST).data.get('field', '')
    parts = str(field_value).split(',')
    data = ','.join(parts)
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
