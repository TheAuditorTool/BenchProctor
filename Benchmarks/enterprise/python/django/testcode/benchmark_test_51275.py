# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def BenchmarkTest51275(request, path_param):
    path_value = path_param
    data = f'{path_value}'
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
