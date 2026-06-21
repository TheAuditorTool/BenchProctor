# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
import defusedxml.ElementTree


@dataclass
class FormData:
    payload: str

def BenchmarkTest09780(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = FormData(payload=ua_value).payload
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
