# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest47666(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = '%s' % str(field_value)
    globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
