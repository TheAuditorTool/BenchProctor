# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import re


def BenchmarkTest17510(request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(config_value).replace('\r', '').replace('\n', ''))
    logging.info('User action: ' + str(processed))
    return JsonResponse({"saved": True})
