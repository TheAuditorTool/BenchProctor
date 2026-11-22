# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
import json


def BenchmarkTest00200(request):
    json_value = json.loads(request.body or b'{}').get('payload', '')
    data = (lambda v: v.strip())(json_value)
    match = re.match(r'^[^@]+@([^@]+)$', str(data))
    domain = match.group(1)
    return JsonResponse({'domain': domain}, status=200)
