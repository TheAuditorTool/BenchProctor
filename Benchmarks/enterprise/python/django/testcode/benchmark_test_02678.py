# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest02678(request):
    xml_value = request.body.decode('utf-8')
    data = FormData(payload=xml_value).payload
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return JsonResponse({"saved": True})
