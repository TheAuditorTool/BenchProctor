# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest25558(request):
    field_value = UserForm(request.POST).data.get('field', '')
    def normalize(value):
        return value.strip()
    data = normalize(field_value)
    os.chmod('/var/app/data/' + str(data), 0o777)
    return JsonResponse({"saved": True})
