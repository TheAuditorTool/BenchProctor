# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import json


def BenchmarkTest49721(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    parts = []
    for token in str(json_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
