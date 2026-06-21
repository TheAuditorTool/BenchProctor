# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from urllib.parse import unquote
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest55034(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = unquote(field_value)
    os.setuid(int(str(data)) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
