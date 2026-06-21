# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest76587(request):
    query_array = request.GET.getlist('items')[0] if request.GET.getlist('items') else ''
    reader = make_reader(query_array)
    data = reader()
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
