# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
import json


def BenchmarkTest00225(request):
    json_value = json.loads(request.body or b'{}').get('payload', '')
    data, _sep, _rest = str(json_value).partition('\x00')
    match = re.match(r'^[^@]+@([^@]+)$', str(data))
    domain = match.group(1)
    return JsonResponse({'domain': domain}, status=200)
