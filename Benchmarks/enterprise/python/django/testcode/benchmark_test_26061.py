# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def BenchmarkTest26061(request, path_param):
    path_value = path_param
    data = ' '.join(str(path_value).split())
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
