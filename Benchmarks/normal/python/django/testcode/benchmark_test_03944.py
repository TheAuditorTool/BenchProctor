# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import re


def to_text(value):
    return str(value).strip()

def BenchmarkTest03944(request):
    xml_value = request.body.decode('utf-8')
    data = to_text(xml_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    logging.info('User action: ' + str(processed))
    return JsonResponse({"saved": True})
