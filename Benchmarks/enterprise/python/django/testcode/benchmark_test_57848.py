# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def BenchmarkTest57848(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    logging.info('User action: ' + str(header_value))
    return JsonResponse({"saved": True})
