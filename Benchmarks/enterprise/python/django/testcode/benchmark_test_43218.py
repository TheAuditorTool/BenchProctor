# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest43218(request):
    field_value = UserForm(request.POST).data.get('field', '')
    globals()['counter'] = int(field_value)
    return JsonResponse({"saved": True})
