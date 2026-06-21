# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest09542(request):
    user_id = request.GET.get('id', '')
    reader = make_reader(user_id)
    data = reader()
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
