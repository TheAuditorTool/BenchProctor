# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def BenchmarkTest53717(request):
    query_array = request.GET.getlist('items')[0] if request.GET.getlist('items') else ''
    data = '{}'.format(query_array)
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
