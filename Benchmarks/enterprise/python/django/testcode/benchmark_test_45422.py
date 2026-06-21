# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest45422(request, path_param):
    path_value = path_param
    reader = make_reader(path_value)
    data = reader()
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
