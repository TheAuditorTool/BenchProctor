# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import re


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest48623(request, path_param):
    path_value = path_param
    reader = make_reader(path_value)
    data = reader()
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(data).replace('\r', '').replace('\n', ''))
    logging.info('User action: ' + str(processed))
    return JsonResponse({"saved": True})
