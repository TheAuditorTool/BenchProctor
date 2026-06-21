# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def BenchmarkTest80352(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    prefix = ''
    data = prefix + str(referer_value)
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
