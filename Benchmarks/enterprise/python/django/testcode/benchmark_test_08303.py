# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import shlex
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest08303(request):
    field_value = UserForm(request.POST).data.get('field', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(field_value)
    data = collected
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
