# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def BenchmarkTest06873(request):
    query_array = request.GET.getlist('items')[0] if request.GET.getlist('items') else ''
    pending = list(str(query_array).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
