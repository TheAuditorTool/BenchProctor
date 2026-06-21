# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
import defusedxml.ElementTree


@dataclass
class FormData:
    payload: str

def BenchmarkTest22714(request):
    raw_body = request.body.decode('utf-8')
    data = FormData(payload=raw_body).payload
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
