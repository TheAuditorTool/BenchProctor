# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
from app_runtime import mq_client


def BenchmarkTest66301(request):
    msg_value = mq_client.get_message().body
    parts = str(msg_value).split(',')
    data = ','.join(parts)
    yaml.safe_load(data)
    return JsonResponse({"saved": True})
