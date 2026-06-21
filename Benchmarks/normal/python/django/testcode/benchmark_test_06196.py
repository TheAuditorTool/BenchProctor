# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def BenchmarkTest06196(request, path_param):
    path_value = path_param
    def normalize(value):
        return value.strip()
    data = normalize(path_value)
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
