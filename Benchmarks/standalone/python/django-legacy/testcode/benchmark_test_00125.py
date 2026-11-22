# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


def BenchmarkTest00125(request):
    raw_body = request.body.decode('utf-8')
    parts = []
    for token in str(raw_body).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    match = re.match(r'^[^@]+@([^@]+)$', str(data))
    if match is None:
        return JsonResponse({'error': 'not an email address'}, status=400)
    domain = match.group(1)
    return JsonResponse({'domain': domain}, status=200)
