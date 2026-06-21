# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def BenchmarkTest75636(request, path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
