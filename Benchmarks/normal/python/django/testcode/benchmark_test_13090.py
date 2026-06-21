# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import shlex
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest13090(request):
    xml_value = request.body.decode('utf-8')
    data = FormData(payload=xml_value).payload
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
