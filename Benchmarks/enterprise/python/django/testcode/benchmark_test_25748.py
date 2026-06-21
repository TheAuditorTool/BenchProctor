# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def BenchmarkTest25748(request):
    query_array = request.GET.getlist('items')[0] if request.GET.getlist('items') else ''
    data = query_array if query_array else 'default'
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
