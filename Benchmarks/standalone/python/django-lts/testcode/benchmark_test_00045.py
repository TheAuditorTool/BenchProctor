# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest00045(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = '%s' % str(origin_value)
    parsed = json.loads(data)
    return JsonResponse({'parsed': str(parsed)}, status=200)
