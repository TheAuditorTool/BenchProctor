# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
from dataclasses import dataclass
from app_runtime import mq_client


@dataclass
class FormData:
    payload: str

def BenchmarkTest01339(request):
    msg_value = mq_client.get_message().body
    data = FormData(payload=msg_value).payload
    yaml.safe_load(data)
    return JsonResponse({"saved": True})
