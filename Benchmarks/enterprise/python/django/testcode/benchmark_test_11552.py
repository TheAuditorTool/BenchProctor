# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def BenchmarkTest11552(request):
    query_array = request.GET.getlist('items')[0] if request.GET.getlist('items') else ''
    parts = []
    for token in str(query_array).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
