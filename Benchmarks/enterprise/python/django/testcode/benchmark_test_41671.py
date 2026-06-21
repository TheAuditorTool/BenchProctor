# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def coalesce_blank(value):
    return value or ''

def BenchmarkTest41671(request):
    query_array = request.GET.getlist('items')[0] if request.GET.getlist('items') else ''
    data = coalesce_blank(query_array)
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
