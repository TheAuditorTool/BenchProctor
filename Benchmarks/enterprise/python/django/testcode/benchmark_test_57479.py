# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import re
import json


def BenchmarkTest57479(request):
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    try:
        data = json.loads(yaml_value).get('value', yaml_value)
    except (json.JSONDecodeError, AttributeError):
        data = yaml_value
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(data).replace('\r', '').replace('\n', ''))
    logging.info('User action: ' + str(processed))
    return JsonResponse({"saved": True})
