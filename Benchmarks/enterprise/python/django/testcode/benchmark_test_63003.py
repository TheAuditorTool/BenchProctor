# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import re
import json
import subprocess


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest63003(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = RequestPayload(graphql_var).value
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    subprocess.run([str(processed), '--status'], shell=False)
    return JsonResponse({"saved": True})
