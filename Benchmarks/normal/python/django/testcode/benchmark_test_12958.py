# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
import tempfile


@dataclass
class FormData:
    payload: str

def BenchmarkTest12958(request):
    raw_body = request.body.decode('utf-8')
    data = FormData(payload=raw_body).payload
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
