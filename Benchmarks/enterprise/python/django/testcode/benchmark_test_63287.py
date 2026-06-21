# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest63287(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = default_blank(host_value)
    processed = data[:64]
    logging.info('User action: ' + str(processed))
    return JsonResponse({"saved": True})
