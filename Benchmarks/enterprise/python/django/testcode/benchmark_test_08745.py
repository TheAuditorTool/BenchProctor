# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def BenchmarkTest08745(request):
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    data = '{}'.format(prop_value)
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
