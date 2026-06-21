# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
from urllib.parse import unquote


def BenchmarkTest17197(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = unquote(referer_value)
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
