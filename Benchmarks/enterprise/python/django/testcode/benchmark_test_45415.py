# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import tempfile
from dataclasses import dataclass
import os


@dataclass
class FormData:
    payload: str

def BenchmarkTest45415(request):
    user_id = request.GET.get('id', '')
    data = FormData(payload=user_id).payload
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
