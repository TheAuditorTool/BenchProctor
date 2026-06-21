# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest30542(request):
    raw_body = request.body.decode('utf-8')
    data = '{}'.format(raw_body)
    json.loads(data)
    return JsonResponse({"saved": True})
