# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest37817(request, path_param):
    path_value = path_param
    data = FormData(payload=path_value).payload
    os.system('echo ' + str(data))
    return JsonResponse({"saved": True})
