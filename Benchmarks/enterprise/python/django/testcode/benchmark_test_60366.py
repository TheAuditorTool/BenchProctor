# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
import socket


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest60366(request):
    field_value = UserForm(request.POST).data.get('field', '')
    pending = list(str(field_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    s = socket.create_connection((str(data), 80))
    s.close()
    return JsonResponse({"saved": True})
