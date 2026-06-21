# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest76505(request):
    raw_body = request.body.decode('utf-8')
    data = FormData(payload=raw_body).payload
    eval(str(data))
    return JsonResponse({"saved": True})
