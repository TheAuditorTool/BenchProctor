# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import shlex
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest77997(request):
    field_value = UserForm(request.POST).data.get('field', '')
    def normalize(value):
        return value.strip()
    data = normalize(field_value)
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
