# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest09703(request):
    host_value = request.META.get('HTTP_HOST', '')
    reader = make_reader(host_value)
    data = reader()
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
