# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


def BenchmarkTest00248(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = ' '.join(str(origin_value).split())
    match = re.match(r'^[^@]+@([^@]+)$', str(data))
    if match is None:
        return JsonResponse({'error': 'not an email address'}, status=400)
    domain = match.group(1)
    return JsonResponse({'domain': domain}, status=200)
