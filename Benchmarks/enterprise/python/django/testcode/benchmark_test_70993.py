# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def BenchmarkTest70993(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    logging.info('User action: ' + str(ua_value))
    return JsonResponse({"saved": True})
