# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
import ctypes


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest16079(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = (lambda v: v.strip())(field_value)
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return JsonResponse({'wrapped': wrapped}, status=200)
