# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest00555(request):
    field_value = UserForm(request.POST).data.get('field', '')
    os.chmod('/var/app/data/' + str(field_value), 0o777)
    return JsonResponse({"saved": True})
