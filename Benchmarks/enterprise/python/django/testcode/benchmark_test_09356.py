# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import tempfile
from dataclasses import dataclass
import os


@dataclass
class FormData:
    payload: str

def BenchmarkTest09356(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = FormData(payload=referer_value).payload
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
