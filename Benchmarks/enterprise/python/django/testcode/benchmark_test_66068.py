# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest66068(request):
    field_value = UserForm(request.POST).data.get('field', '')
    size = min(int(field_value) if str(field_value).isdigit() else 0, 1024)
    data = bytearray(size)
    return JsonResponse({"saved": True})
