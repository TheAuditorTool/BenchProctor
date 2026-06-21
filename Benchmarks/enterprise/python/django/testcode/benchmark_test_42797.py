# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest42797(request):
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    data = default_blank(yaml_value)
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
