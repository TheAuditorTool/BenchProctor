# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import tempfile
from django import forms
import os


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest28076(request):
    field_value = UserForm(request.POST).data.get('field', '')
    kind = 'json' if str(field_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = field_value
            data = parsed
        case _:
            data = field_value
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
