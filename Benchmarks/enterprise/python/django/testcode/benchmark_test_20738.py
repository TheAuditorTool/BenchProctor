# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def BenchmarkTest20738(request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    data = '{}'.format(config_value)
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
