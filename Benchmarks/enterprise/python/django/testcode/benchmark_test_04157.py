# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest04157(request, path_param):
    path_value = path_param
    data = default_blank(path_value)
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
