# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest14122(request):
    field_value = UserForm(request.POST).data.get('field', '')
    request.session['data'] = str(field_value)
    return JsonResponse({"saved": True})
