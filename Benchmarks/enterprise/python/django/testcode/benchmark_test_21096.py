# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def BenchmarkTest21096(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(origin_value)
    data = collected
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
