# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def BenchmarkTest67330(request):
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    logging.info('User action: ' + str(prop_value))
    return JsonResponse({"saved": True})
