# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
from urllib.parse import unquote


def BenchmarkTest02411(request, path_param):
    path_value = path_param
    data = unquote(path_value)
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
