# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest09938(request):
    xml_value = request.body.decode('utf-8')
    data = FormData(payload=xml_value).payload
    os.system('echo ' + str(data))
    return JsonResponse({"saved": True})
