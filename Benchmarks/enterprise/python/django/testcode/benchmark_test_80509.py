# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest80509(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = '%s' % (field_value,)
    os.system('echo ' + str(data))
    return JsonResponse({"saved": True})
