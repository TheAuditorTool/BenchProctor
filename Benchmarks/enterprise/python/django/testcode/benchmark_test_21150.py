# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest21150(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data, _sep, _rest = str(field_value).partition('\x00')
    os.remove(str(data))
    return JsonResponse({"saved": True})
