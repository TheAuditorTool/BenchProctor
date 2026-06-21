# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import re


def BenchmarkTest07663(request):
    query_array = request.GET.getlist('items')[0] if request.GET.getlist('items') else ''
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(query_array)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = query_array
    logging.info('User action: ' + str(processed))
    return JsonResponse({"saved": True})
