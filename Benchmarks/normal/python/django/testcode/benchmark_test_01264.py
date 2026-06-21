# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


def relay_value(value):
    return value

def BenchmarkTest01264(request):
    raw_body = request.body.decode('utf-8')
    data = relay_value(raw_body)
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    if re.search('[a-zA-Z0-9_-]+', str(processed)):
        return JsonResponse({'validated': str(processed)}, status=200)
    return JsonResponse({"saved": True})
