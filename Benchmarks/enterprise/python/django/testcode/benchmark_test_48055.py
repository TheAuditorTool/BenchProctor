# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def BenchmarkTest48055(request):
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    data = ' '.join(str(yaml_value).split())
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
