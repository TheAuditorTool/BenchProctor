# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def BenchmarkTest73142(request):
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    data = ' '.join(str(prop_value).split())
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
