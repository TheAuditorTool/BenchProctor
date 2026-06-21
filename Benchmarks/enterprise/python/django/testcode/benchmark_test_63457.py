# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import json


def BenchmarkTest63457(request):
    query_array = request.GET.getlist('items')[0] if request.GET.getlist('items') else ''
    try:
        data = json.loads(query_array).get('value', query_array)
    except (json.JSONDecodeError, AttributeError):
        data = query_array
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
