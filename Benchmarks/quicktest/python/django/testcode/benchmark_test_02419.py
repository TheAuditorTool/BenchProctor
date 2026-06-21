# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
from app_runtime import mq_client


request_state: dict[str, str] = {}

def BenchmarkTest02419(request):
    msg_value = mq_client.get_message().body
    request_state['last_input'] = msg_value
    data = request_state['last_input']
    yaml.safe_load(data)
    return JsonResponse({"saved": True})
