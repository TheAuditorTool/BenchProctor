# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest58388(request):
    upload_name = request.FILES['upload'].name
    reader = make_reader(upload_name)
    data = reader()
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
