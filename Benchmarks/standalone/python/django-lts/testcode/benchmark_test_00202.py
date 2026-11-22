# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest00202(request):
    json_value = json.loads(request.body or b'{}').get('payload', '')
    request.session.update({'data': str(json_value)})
    return JsonResponse({"saved": True})
