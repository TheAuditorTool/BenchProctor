# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest39603(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = str(field_value).replace('\x00', '')
    os.chmod('/var/app/data/' + str(data), 0o777)
    return JsonResponse({"saved": True})
