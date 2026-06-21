# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest08323(request):
    user_id = request.GET.get('id', '')
    data = FormData(payload=user_id).payload
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return JsonResponse({"saved": True})
