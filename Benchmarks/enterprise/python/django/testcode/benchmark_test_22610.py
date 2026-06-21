# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def BenchmarkTest22610(request):
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    data, _sep, _rest = str(prop_value).partition('\x00')
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
