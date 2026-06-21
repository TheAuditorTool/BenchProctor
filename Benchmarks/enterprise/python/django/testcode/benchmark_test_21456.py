# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import re
import json


def BenchmarkTest21456(request):
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    try:
        data = json.loads(prop_value).get('value', prop_value)
    except (json.JSONDecodeError, AttributeError):
        data = prop_value
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(data).replace('\r', '').replace('\n', ''))
    logging.info('User action: ' + str(processed))
    return JsonResponse({"saved": True})
