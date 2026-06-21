# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import re


def BenchmarkTest32257(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', header_value):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = header_value
    logging.info('User action: ' + str(processed))
    return JsonResponse({"saved": True})
