# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import os


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest75625(request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    reader = make_reader(dotenv_value)
    data = reader()
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
