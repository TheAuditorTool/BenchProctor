# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
import tempfile


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest51032(request):
    field_value = UserForm(request.POST).data.get('field', '')
    if field_value:
        data = field_value
    else:
        data = ''
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
