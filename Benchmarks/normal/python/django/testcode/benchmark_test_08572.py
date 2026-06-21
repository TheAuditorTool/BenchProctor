# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import re


def relay_value(value):
    return value

def BenchmarkTest08572(request):
    raw_body = request.body.decode('utf-8')
    data = relay_value(raw_body)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    logging.info('User action: ' + str(processed))
    return JsonResponse({"saved": True})
