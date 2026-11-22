# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest00110(request):
    json_value = json.loads(request.body or b'{}').get('payload', '')
    data = json.loads(json_value).get('value', '')
    _coerced = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    processed = _coerced
    eval(str(processed))
    return JsonResponse({"saved": True})
