# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def BenchmarkTest25283(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = f'{host_value:.200s}'
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
