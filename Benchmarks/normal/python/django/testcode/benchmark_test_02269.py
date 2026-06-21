# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def BenchmarkTest02269(request):
    raw_body = request.body.decode('utf-8')
    data = ' '.join(str(raw_body).split())
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
