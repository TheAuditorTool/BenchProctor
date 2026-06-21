# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from app_runtime import mq_client


def BenchmarkTest75236(request):
    msg_value = mq_client.get_message().body
    kind = 'json' if str(msg_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = msg_value
            data = parsed
        case _:
            data = msg_value
    requests.get(str(data))
    return JsonResponse({"saved": True})
