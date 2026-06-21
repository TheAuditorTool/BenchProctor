# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
from app_runtime import mq_client


def BenchmarkTest54388(request):
    msg_value = mq_client.get_message().body
    data = (lambda v: v.strip())(msg_value)
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return JsonResponse({"saved": True})
