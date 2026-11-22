# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


def BenchmarkTest00131(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    match = re.match(r'^[^@]+@([^@]+)$', str(forwarded_ip))
    if match is None:
        return JsonResponse({'error': 'not an email address'}, status=400)
    domain = match.group(1)
    return JsonResponse({'domain': domain}, status=200)
