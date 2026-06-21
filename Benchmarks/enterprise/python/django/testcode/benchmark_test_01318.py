# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import json


def BenchmarkTest01318(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    try:
        data = json.loads(referer_value).get('value', referer_value)
    except (json.JSONDecodeError, AttributeError):
        data = referer_value
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
