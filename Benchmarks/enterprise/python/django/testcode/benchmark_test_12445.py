# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from app_runtime import mq_client


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest12445(request):
    msg_value = mq_client.get_message().body
    reader = make_reader(msg_value)
    data = reader()
    json.loads(data)
    return JsonResponse({"saved": True})
