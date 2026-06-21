# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
from app_runtime import mq_client


def BenchmarkTest73655(request):
    msg_value = mq_client.get_message().body
    data = str(msg_value).replace('\x00', '')
    yaml.safe_load(data)
    return JsonResponse({"saved": True})
