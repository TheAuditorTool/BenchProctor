# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def BenchmarkTest02122(request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    logging.info('User action: ' + str(config_value))
    return JsonResponse({"saved": True})
