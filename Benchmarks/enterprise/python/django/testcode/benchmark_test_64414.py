# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def BenchmarkTest64414(request, path_param):
    path_value = path_param
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(path_value)
    data = collected
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
