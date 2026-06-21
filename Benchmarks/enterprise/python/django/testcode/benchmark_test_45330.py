# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
from urllib.parse import unquote


def BenchmarkTest45330(request):
    query_array = request.GET.getlist('items')[0] if request.GET.getlist('items') else ''
    data = unquote(query_array)
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
