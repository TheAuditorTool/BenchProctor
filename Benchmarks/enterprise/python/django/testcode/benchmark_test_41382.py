# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def BenchmarkTest41382(request):
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    def normalize(value):
        return value.strip()
    data = normalize(yaml_value)
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
