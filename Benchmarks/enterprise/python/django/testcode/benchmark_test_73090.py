# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
from django.http import HttpResponse


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest73090(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = f'{field_value}'
    return HttpResponse('<!-- diagnostic build token: ' + str(data) + ' -->', content_type='text/html')
