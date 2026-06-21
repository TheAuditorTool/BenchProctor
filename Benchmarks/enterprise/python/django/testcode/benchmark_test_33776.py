# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import tempfile
from django import forms
import os


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest33776(request):
    field_value = UserForm(request.POST).data.get('field', '')
    pending = list(str(field_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
