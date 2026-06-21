# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def to_text(value):
    return str(value).strip()

def BenchmarkTest46334(request):
    raw_body = request.body.decode('utf-8')
    data = to_text(raw_body)
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    logging.info('User action: ' + str(processed))
    return JsonResponse({"saved": True})
