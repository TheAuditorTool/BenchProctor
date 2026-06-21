# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)
def coalesce_blank(value):
    return value or ''

def BenchmarkTest08545(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = coalesce_blank(field_value)
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return JsonResponse({"saved": True})
