# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def BenchmarkTest80692(request):
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    if prop_value:
        data = prop_value
    else:
        data = ''
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
