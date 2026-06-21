# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import os


def to_text(value):
    return str(value).strip()

def BenchmarkTest38450(request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    data = to_text(dotenv_value)
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
