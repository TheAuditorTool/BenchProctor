# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import re


def BenchmarkTest62598(request):
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(prop_value).replace('\r', '').replace('\n', ''))
    logging.info('User action: ' + str(processed))
    return JsonResponse({"saved": True})
