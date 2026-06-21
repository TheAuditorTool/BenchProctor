# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
import defusedxml.ElementTree


@dataclass
class FormData:
    payload: str

def BenchmarkTest66811(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = FormData(payload=forwarded_ip).payload
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
