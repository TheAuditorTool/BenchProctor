# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
import pickle


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest02804(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = field_value if field_value else 'default'
    pickle.loads(data.encode('latin-1'))
    return JsonResponse({"saved": True})
