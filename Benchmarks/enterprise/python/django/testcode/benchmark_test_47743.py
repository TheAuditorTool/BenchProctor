# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import re


def BenchmarkTest47743(request):
    user_id = request.GET.get('id', '')
    data = f'{user_id:.200s}'
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    logging.info('User action: ' + str(processed))
    return JsonResponse({"saved": True})
