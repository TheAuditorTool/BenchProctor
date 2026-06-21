# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def BenchmarkTest18460(request):
    query_array = request.GET.getlist('items')[0] if request.GET.getlist('items') else ''
    parts = str(query_array).split(',')
    data = ','.join(parts)
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
