# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from urllib.parse import unquote
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest06048(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = unquote(field_value)
    os.remove(str(data))
    return JsonResponse({"saved": True})
