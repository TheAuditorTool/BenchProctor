# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def BenchmarkTest00156(request):
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(yaml_value)
    data = collected
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
