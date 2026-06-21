# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def normalise_input(value):
    return value.strip()

def BenchmarkTest55158(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = normalise_input(origin_value)
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
