# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import tempfile
from dataclasses import dataclass
import os


@dataclass
class FormData:
    payload: str

def BenchmarkTest70459(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = FormData(payload=auth_header).payload
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
