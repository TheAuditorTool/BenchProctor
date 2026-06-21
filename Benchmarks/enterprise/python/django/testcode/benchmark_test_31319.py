# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import re


def BenchmarkTest31319(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', forwarded_ip):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = forwarded_ip
    logging.info('User action: ' + str(processed))
    return JsonResponse({"saved": True})
