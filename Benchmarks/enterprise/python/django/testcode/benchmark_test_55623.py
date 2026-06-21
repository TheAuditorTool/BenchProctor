# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import tempfile
from django import forms
import os


class UserForm(forms.Form):
    field = forms.CharField(required=False)
class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest55623(request):
    field_value = UserForm(request.POST).data.get('field', '')
    ctx = RequestContext(field_value)
    data = ctx.payload
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
