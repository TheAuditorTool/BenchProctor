# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def BenchmarkTest04428(request):
    query_array = request.GET.getlist('items')[0] if request.GET.getlist('items') else ''
    kind = 'json' if str(query_array).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = query_array
            data = parsed
        case _:
            data = query_array
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
