# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
from django import forms
from django.http import HttpResponse
import os


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest10124(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = '%s' % str(field_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    link_path = os.path.join('/var/app/data', str(processed))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
