# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest23858(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = '{}'.format(field_value)
    eval(str(data))
    return JsonResponse({"saved": True})
