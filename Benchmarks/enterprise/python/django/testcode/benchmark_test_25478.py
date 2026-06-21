# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest25478(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = str(field_value).replace('\x00', '')
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
