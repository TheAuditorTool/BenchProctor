# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest60670(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    parts = str(origin_value).split(',')
    data = ','.join(parts)
    json.loads(data)
    return JsonResponse({"saved": True})
