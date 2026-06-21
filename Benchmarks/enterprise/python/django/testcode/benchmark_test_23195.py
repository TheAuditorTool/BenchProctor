# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def BenchmarkTest23195(request):
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    data = '%s' % (yaml_value,)
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
