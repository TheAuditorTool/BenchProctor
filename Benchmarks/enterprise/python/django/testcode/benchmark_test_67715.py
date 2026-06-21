# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from app_runtime import mq_client


def BenchmarkTest67715(request):
    msg_value = mq_client.get_message().body
    data, _sep, _rest = str(msg_value).partition('\x00')
    requests.get(str(data))
    return JsonResponse({"saved": True})
