# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
import defusedxml.ElementTree


@dataclass
class FormData:
    payload: str

def BenchmarkTest43703(request):
    xml_value = request.body.decode('utf-8')
    data = FormData(payload=xml_value).payload
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
