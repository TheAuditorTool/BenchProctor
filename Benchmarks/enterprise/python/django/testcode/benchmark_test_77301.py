# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import os


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest77301(request):
    env_value = os.environ.get('USER_INPUT', '')
    reader = make_reader(env_value)
    data = reader()
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
