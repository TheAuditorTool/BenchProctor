# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest00299(request):
    json_value = json.loads(request.body or b'{}').get('payload', '')
    data = (lambda v: v.strip())(json_value)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
