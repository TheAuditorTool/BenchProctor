# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
import json
from app_runtime import mq_client


@dataclass
class FormData:
    payload: str

def BenchmarkTest79827(request):
    msg_value = mq_client.get_message().body
    data = FormData(payload=msg_value).payload
    json.loads(data)
    return JsonResponse({"saved": True})
