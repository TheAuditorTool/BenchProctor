# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def BenchmarkTest70148(request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    data = (lambda v: v.strip())(config_value)
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
