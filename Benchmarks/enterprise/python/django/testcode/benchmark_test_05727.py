# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def BenchmarkTest05727(request):
    query_array = request.GET.getlist('items')[0] if request.GET.getlist('items') else ''
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(query_array)
    data = collected
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
