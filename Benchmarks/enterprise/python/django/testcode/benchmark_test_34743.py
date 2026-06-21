# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def BenchmarkTest34743(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    logging.info('User action: ' + str(referer_value))
    return JsonResponse({"saved": True})
