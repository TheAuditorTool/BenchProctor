# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
import socket


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest05820(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = str(field_value).replace('\x00', '')
    s = socket.create_connection((str(data), 80))
    s.close()
    return JsonResponse({"saved": True})
