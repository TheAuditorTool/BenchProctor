# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
import defusedxml.ElementTree


@dataclass
class FormData:
    payload: str

def BenchmarkTest66122(request, path_param):
    path_value = path_param
    data = FormData(payload=path_value).payload
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
