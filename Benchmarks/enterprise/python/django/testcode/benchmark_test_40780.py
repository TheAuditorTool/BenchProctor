# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def BenchmarkTest40780(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    if origin_value:
        data = origin_value
    else:
        data = ''
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
