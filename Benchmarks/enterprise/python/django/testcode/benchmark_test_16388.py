# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def BenchmarkTest16388(request):
    query_array = request.GET.getlist('items')[0] if request.GET.getlist('items') else ''
    def normalize(value):
        return value.strip()
    data = normalize(query_array)
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
