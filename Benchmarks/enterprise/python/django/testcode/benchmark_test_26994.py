# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest26994(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = '%s' % (field_value,)
    requests.get(str(data))
    return JsonResponse({"saved": True})
