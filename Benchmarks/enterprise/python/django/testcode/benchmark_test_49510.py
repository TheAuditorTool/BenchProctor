# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
import re


@dataclass
class FormData:
    payload: str

def BenchmarkTest49510(request, path_param):
    path_value = path_param
    data = FormData(payload=path_value).payload
    if re.search('[a-zA-Z0-9_-]+', str(data)):
        return JsonResponse({'validated': str(data)}, status=200)
    return JsonResponse({"saved": True})
