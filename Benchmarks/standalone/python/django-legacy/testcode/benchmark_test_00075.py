# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw if self._raw is not None else ''

def BenchmarkTest00075(request):
    graphql_var = json.loads(request.body or b'{}').get('variables', {}).get('input', '')
    data = RequestPayload(graphql_var).value
    code = compile(str(data), '<rule>', 'exec')
    exec(code)
    return JsonResponse({"saved": True})
