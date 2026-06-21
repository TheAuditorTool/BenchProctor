# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def normalise_input(value):
    return value.strip()

def BenchmarkTest12372(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = normalise_input(host_value)
    processed = data[:64]
    logging.info('User action: ' + str(processed))
    return JsonResponse({"saved": True})
