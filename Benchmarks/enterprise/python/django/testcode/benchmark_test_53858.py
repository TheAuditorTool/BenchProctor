# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
from dataclasses import dataclass
from app_runtime import redis_client


@dataclass
class FormData:
    payload: str

def BenchmarkTest53858(request):
    redis_value = redis_client.get('user_data')
    data = FormData(payload=redis_value).payload
    yaml.safe_load(data)
    return JsonResponse({"saved": True})
