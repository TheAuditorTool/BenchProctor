# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import re


def BenchmarkTest30359(request):
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    kind = 'json' if str(yaml_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = yaml_value
            data = parsed
        case _:
            data = yaml_value
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    logging.info('User action: ' + str(processed))
    return JsonResponse({"saved": True})
