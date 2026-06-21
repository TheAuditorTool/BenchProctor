# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
from django.http import HttpResponse


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest73012(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = field_value if field_value else 'default'
    return HttpResponse('<html><body><h1>' + str(data) + '</h1></body></html>', content_type='text/html')
