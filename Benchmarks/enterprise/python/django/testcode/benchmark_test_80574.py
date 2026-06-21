# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def BenchmarkTest80574(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    logging.info('User action: ' + str(forwarded_ip))
    return JsonResponse({"saved": True})
