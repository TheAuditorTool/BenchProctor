# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading
import json


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest31274(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = RequestPayload(graphql_var).value
    globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
