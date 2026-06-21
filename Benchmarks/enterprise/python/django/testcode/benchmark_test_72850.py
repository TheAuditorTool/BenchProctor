# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest72850(request):
    field_value = UserForm(request.POST).data.get('field', '')
    with open('/var/uploads/' + str(field_value), 'wb') as fh:
        fh.write(b'data')
    return JsonResponse({"saved": True})
