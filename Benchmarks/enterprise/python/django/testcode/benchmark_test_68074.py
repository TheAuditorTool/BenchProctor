# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def BenchmarkTest68074(request):
    query_array = request.GET.getlist('items')[0] if request.GET.getlist('items') else ''
    if query_array:
        data = query_array
    else:
        data = ''
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
