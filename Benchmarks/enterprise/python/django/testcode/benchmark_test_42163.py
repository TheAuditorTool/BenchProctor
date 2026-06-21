# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import re
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest42163(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = FormData(payload=referer_value).payload
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    logging.info('User action: ' + str(processed))
    return JsonResponse({"saved": True})
