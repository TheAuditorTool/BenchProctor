# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import re


def to_text(value):
    return str(value).strip()

def BenchmarkTest15866(request):
    user_id = request.GET.get('id', '')
    data = to_text(user_id)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    logging.info('User action: ' + str(processed))
    return JsonResponse({"saved": True})
