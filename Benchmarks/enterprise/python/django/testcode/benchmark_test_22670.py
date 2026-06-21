# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from app_runtime import mq_client


def BenchmarkTest22670(request):
    msg_value = mq_client.get_message().body
    data, _sep, _rest = str(msg_value).partition('\x00')
    json.loads(data)
    return JsonResponse({"saved": True})
