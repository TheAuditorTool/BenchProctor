# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def BenchmarkTest01088(request):
    query_array = request.GET.getlist('items')[0] if request.GET.getlist('items') else ''
    data, _sep, _rest = str(query_array).partition('\x00')
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
