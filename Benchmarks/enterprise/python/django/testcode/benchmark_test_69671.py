# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import re


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest69671(request):
    raw_body = request.body.decode('utf-8')
    data = default_blank(raw_body)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    logging.info('User action: ' + str(processed))
    return JsonResponse({"saved": True})
