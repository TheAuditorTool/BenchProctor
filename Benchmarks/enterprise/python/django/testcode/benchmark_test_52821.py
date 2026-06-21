# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def BenchmarkTest52821(request):
    raw_body = request.body.decode('utf-8')
    logging.info('User action: ' + str(raw_body))
    return JsonResponse({"saved": True})
