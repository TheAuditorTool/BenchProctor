# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
import defusedxml.ElementTree


@dataclass
class FormData:
    payload: str

def BenchmarkTest00482(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = FormData(payload=origin_value).payload
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
