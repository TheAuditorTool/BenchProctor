# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
from django.http import HttpResponse
import unicodedata


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest14726(request):
    field_value = UserForm(request.POST).data.get('field', '')
    parts = str(field_value).split(',')
    data = ','.join(parts)
    normalized = unicodedata.normalize('NFKC', str(data))
    return HttpResponse('<p>' + normalized + '</p>', content_type='text/html')
