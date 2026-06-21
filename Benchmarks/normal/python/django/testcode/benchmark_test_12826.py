# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import re


def relay_value(value):
    return value

def BenchmarkTest12826(request, path_param):
    path_value = path_param
    data = relay_value(path_value)
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(data).replace('\r', '').replace('\n', ''))
    logging.info('User action: ' + str(processed))
    return JsonResponse({"saved": True})
