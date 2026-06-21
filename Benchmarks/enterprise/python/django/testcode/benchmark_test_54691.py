# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def BenchmarkTest54691(request):
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    data = (lambda v: v.strip())(yaml_value)
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
