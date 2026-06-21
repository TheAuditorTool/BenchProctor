# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def BenchmarkTest68749(request):
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    if yaml_value:
        data = yaml_value
    else:
        data = ''
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
