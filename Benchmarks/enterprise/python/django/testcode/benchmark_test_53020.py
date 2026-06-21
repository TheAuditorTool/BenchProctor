# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def BenchmarkTest53020(request):
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    data, _sep, _rest = str(yaml_value).partition('\x00')
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
