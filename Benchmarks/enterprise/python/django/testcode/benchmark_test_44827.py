# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import json


def BenchmarkTest44827(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = '{}'.format(json_value)
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
