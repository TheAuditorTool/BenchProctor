# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
import ctypes


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest57022(request):
    field_value = UserForm(request.POST).data.get('field', '')
    kind = 'json' if str(field_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = field_value
            data = parsed
        case _:
            data = field_value
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return JsonResponse({'wrapped': wrapped}, status=200)
