# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from urllib.parse import urlparse
from django import forms
from django.http import HttpResponse


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest60683(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = str(field_value).replace('\x00', '')
    parsed = urlparse(data)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    target_url = data
    return HttpResponse('<script src="' + str(target_url) + '"></script>', content_type='text/html')
