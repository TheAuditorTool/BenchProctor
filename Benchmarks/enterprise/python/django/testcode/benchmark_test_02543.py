# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
import os
import tempfile


@dataclass
class FormData:
    payload: str

def BenchmarkTest02543(request):
    upload_name = request.FILES['upload'].name
    data = FormData(payload=upload_name).payload
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    os.chmod(path, 0o777)
    return JsonResponse({"saved": True})
