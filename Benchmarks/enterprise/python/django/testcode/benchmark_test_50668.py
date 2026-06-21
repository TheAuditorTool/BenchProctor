# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def BenchmarkTest50668(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = f'{referer_value}'
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
