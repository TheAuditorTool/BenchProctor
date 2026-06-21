# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def BenchmarkTest09756(request):
    xml_value = request.body.decode('utf-8')
    prefix = ''
    data = prefix + str(xml_value)
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    logging.info('User action: ' + str(processed))
    return JsonResponse({"saved": True})
