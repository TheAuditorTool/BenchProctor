# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import json


def BenchmarkTest43577(request):
    raw_body = request.body.decode('utf-8')
    data = json.loads(raw_body).get('value', '')
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
