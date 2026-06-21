# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
import socket


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest39695(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data, _sep, _rest = str(field_value).partition('\x00')
    s = socket.create_connection((str(data), 80))
    s.close()
    return JsonResponse({"saved": True})
