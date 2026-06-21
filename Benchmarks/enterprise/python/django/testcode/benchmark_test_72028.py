# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)
def relay_value(value):
    return value

def BenchmarkTest72028(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = relay_value(field_value)
    os.remove(str(data))
    return JsonResponse({"saved": True})
