# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
from urllib.parse import unquote


def BenchmarkTest20523(request, path_param):
    path_value = path_param
    data = unquote(path_value)
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    logging.info('User action: ' + str(processed))
    return JsonResponse({"saved": True})
