# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def BenchmarkTest36381(request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    data, _sep, _rest = str(config_value).partition('\x00')
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
