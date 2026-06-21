# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def BenchmarkTest76155(request):
    query_array = request.GET.getlist('items')[0] if request.GET.getlist('items') else ''
    data = f'{query_array:.200s}'
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
