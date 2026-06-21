# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
from app_runtime import mq_client


def BenchmarkTest77737(request):
    msg_value = mq_client.get_message().body
    data, _sep, _rest = str(msg_value).partition('\x00')
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return JsonResponse({"saved": True})
