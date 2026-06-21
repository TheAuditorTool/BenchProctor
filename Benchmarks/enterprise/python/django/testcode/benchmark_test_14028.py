# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import re


def normalise_input(value):
    return value.strip()

def BenchmarkTest14028(request):
    user_id = request.GET.get('id', '')
    data = normalise_input(user_id)
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    logging.info('User action: ' + str(processed))
    return JsonResponse({"saved": True})
