# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest72202(request):
    upload_name = request.FILES['upload'].name
    reader = make_reader(upload_name)
    data = reader()
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    logging.info('User action: ' + str(processed))
    return JsonResponse({"saved": True})
