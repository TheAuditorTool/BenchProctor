# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
import pickle


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest42879(request):
    field_value = UserForm(request.POST).data.get('field', '')
    prefix = ''
    data = prefix + str(field_value)
    pickle.loads(data.encode('latin-1'))
    return JsonResponse({"saved": True})
