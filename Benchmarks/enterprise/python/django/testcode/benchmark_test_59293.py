# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def BenchmarkTest59293(request):
    raw_body = request.body.decode('utf-8')
    data = raw_body if raw_body else 'default'
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
