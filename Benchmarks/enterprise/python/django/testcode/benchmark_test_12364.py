# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def relay_value(value):
    return value

def BenchmarkTest12364(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = relay_value(origin_value)
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
