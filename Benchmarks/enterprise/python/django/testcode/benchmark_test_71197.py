# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def BenchmarkTest71197(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = host_value if host_value else 'default'
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
