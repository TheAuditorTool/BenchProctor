# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import os


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest41378(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = RequestPayload(json_value).value
    entries = os.listdir(str(data))
    return JsonResponse({'listing': entries}, status=200)
