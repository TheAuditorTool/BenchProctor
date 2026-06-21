# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
import os
import defusedxml.ElementTree


@dataclass
class FormData:
    payload: str

def BenchmarkTest73644(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = FormData(payload=env_value).payload
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
