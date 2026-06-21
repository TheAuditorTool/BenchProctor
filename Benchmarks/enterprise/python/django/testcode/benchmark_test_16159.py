# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def BenchmarkTest16159(request, path_param):
    path_value = path_param
    data = str(path_value).replace('\x00', '')
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
