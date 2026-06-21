# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect
import json
import urllib.parse


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest60526(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = RequestPayload(json_value).value
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(processed))
    return redirect(target)
