# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def BenchmarkTest79778(request):
    raw_body = request.body.decode('utf-8')
    data = str(raw_body).replace('\x00', '')
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
