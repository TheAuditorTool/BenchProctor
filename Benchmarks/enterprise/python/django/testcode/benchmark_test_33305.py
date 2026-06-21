# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import re


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest33305(request):
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    data = default_blank(yaml_value)
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(data).replace('\r', '').replace('\n', ''))
    logging.info('User action: ' + str(processed))
    return JsonResponse({"saved": True})
