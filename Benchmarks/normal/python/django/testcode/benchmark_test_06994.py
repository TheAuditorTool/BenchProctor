# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest06994(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = RequestPayload(json_value).value
    os.system('echo ' + str(data))
    return JsonResponse({"saved": True})
