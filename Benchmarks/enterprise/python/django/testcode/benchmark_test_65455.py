# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import re


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest65455(request):
    host_value = request.META.get('HTTP_HOST', '')
    reader = make_reader(host_value)
    data = reader()
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(data).replace('\r', '').replace('\n', ''))
    logging.info('User action: ' + str(processed))
    return JsonResponse({"saved": True})
