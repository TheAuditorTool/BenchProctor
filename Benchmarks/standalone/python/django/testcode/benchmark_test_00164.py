# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest00164(request):
    json_value = json.loads(request.body or b'{}').get('payload', '')
    data = '%s' % str(json_value)
    eval(str(data))
    return JsonResponse({"saved": True})
