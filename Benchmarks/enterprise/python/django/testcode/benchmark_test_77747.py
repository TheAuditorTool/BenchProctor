# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest77747(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = f'{field_value}'
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
