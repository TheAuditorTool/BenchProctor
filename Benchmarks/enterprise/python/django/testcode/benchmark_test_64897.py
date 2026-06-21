# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import base64


def BenchmarkTest64897(request):
    raw_body = request.body.decode('utf-8')
    data = base64.b64decode(raw_body).decode('utf-8', 'ignore')
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
