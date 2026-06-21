# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import re


def BenchmarkTest45574(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(ua_value)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = ua_value
    logging.info('User action: ' + str(processed))
    return JsonResponse({"saved": True})
