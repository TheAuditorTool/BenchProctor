# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest30053(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = f'{field_value:.200s}'
    os.remove(str(data))
    return JsonResponse({"saved": True})
