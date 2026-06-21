# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import re


def BenchmarkTest39263(request):
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    parts = []
    for token in str(prop_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    logging.info('User action: ' + str(processed))
    return JsonResponse({"saved": True})
