# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import re


def BenchmarkTest15364(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = ' '.join(str(auth_header).split())
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    logging.info('User action: ' + str(processed))
    return JsonResponse({"saved": True})
