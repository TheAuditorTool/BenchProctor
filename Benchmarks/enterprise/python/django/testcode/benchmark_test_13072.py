# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


def BenchmarkTest13072(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = '{}'.format(ua_value)
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    if re.search('[a-zA-Z0-9_-]+', str(processed)):
        return JsonResponse({'validated': str(processed)}, status=200)
    return JsonResponse({"saved": True})
