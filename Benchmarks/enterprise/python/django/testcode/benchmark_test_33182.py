# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import os


def to_text(value):
    return str(value).strip()

def BenchmarkTest33182(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = to_text(env_value)
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
