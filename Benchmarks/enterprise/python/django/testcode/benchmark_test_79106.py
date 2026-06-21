# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def to_text(value):
    return str(value).strip()

def BenchmarkTest79106(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = to_text(cookie_value)
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    logging.info('User action: ' + str(processed))
    return JsonResponse({"saved": True})
