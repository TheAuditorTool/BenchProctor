# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest43627(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = '%s' % str(field_value)
    os.remove(str(data))
    return JsonResponse({"saved": True})
