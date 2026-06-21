# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from django import forms
from django.http import HttpResponse


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest52936(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = '%s' % (field_value,)
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
