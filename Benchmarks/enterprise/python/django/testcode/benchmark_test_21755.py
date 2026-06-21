# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
import defusedxml.ElementTree


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest21755(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = field_value if field_value else 'default'
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
