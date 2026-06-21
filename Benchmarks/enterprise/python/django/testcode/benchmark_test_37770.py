# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
from django.http import HttpResponse


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest37770(request):
    field_value = UserForm(request.POST).data.get('field', '')
    prefix = ''
    data = prefix + str(field_value)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
