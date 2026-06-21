# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest80143(request):
    raw_body = request.body.decode('utf-8')
    data = FormData(payload=raw_body).payload
    os.remove(str(data))
    return JsonResponse({"saved": True})
