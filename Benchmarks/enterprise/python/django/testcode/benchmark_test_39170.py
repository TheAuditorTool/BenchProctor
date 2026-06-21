# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from app_runtime import mq_client


def BenchmarkTest39170(request):
    msg_value = mq_client.get_message().body
    parts = str(msg_value).split(',')
    data = ','.join(parts)
    json.loads(data)
    return JsonResponse({"saved": True})
