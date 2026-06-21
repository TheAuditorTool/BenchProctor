# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import unquote
from django import forms
import defusedxml.ElementTree


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest05997(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = unquote(field_value)
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
