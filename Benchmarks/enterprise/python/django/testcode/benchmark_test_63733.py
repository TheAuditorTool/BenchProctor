# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest63733(request, path_param):
    path_value = path_param
    data = FormData(payload=path_value).payload
    os.remove(str(data))
    return JsonResponse({"saved": True})
