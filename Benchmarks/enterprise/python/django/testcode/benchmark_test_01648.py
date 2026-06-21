# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import re


def BenchmarkTest01648(request, path_param):
    path_value = path_param
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(path_value).replace('\r', '').replace('\n', ''))
    logging.info('User action: ' + str(processed))
    return JsonResponse({"saved": True})
