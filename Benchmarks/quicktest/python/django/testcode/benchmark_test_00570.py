# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from app_runtime import mq_client


def BenchmarkTest00570(request):
    msg_value = mq_client.get_message().body
    data = f'{msg_value:.200s}'
    requests.get(str(data))
    return JsonResponse({"saved": True})
