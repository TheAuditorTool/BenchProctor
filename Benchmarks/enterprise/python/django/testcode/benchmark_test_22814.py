# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import json


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest22814(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = RequestPayload(graphql_var).value
    digest = str(data).encode().hex()
    return JsonResponse({'digest': str(digest)}, status=200)
