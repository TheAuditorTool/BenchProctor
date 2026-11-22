# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
import base64
import pickle


@dataclass
class FormData:
    payload: str
    content_type: str = 'text/plain'

def BenchmarkTest00131(request):
    raw_body = request.body.decode('utf-8')
    form = FormData(payload=raw_body)
    data = form.payload
    pickle.loads(base64.b64decode(data))
    return JsonResponse({"saved": True})
