# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest59830(request):
    field_value = UserForm(request.POST).data.get('field', '')
    parts = str(field_value).split(',')
    data = ','.join(parts)
    globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
