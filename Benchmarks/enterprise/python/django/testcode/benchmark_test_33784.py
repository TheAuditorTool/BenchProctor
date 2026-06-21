# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def BenchmarkTest33784(request):
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    data = '{}'.format(yaml_value)
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
