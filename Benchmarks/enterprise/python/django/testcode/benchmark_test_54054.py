# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import re


def normalise_input(value):
    return value.strip()

def BenchmarkTest54054(request):
    upload_name = request.FILES['upload'].name
    data = normalise_input(upload_name)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    logging.info('User action: ' + str(processed))
    return JsonResponse({"saved": True})
