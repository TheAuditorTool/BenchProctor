# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def BenchmarkTest49453(request):
    host_value = request.META.get('HTTP_HOST', '')
    logging.info('User action: ' + str(host_value))
    return JsonResponse({"saved": True})
