# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import re


def coalesce_blank(value):
    return value or ''

def BenchmarkTest29995(request):
    upload_name = request.FILES['upload'].name
    data = coalesce_blank(upload_name)
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    logging.info('User action: ' + str(processed))
    return JsonResponse({"saved": True})
