# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from app_runtime import mq_client


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest53108(request):
    msg_value = mq_client.get_message().body
    data = RequestPayload(msg_value).value
    requests.get(str(data))
    return JsonResponse({"saved": True})
