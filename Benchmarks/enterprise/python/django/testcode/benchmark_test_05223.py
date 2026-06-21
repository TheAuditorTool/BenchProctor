# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)
def ensure_str(value):
    return str(value)

def BenchmarkTest05223(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = ensure_str(field_value)
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return JsonResponse({"saved": True})
