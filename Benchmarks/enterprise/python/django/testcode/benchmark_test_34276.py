# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
import os
import tempfile


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest34276(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = f'{field_value:.200s}'
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    os.chmod(path, 0o777)
    return JsonResponse({"saved": True})
