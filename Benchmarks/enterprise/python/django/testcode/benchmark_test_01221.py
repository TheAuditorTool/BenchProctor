# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def BenchmarkTest01221(request):
    raw_body = request.body.decode('utf-8')
    data = f'{raw_body:.200s}'
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
