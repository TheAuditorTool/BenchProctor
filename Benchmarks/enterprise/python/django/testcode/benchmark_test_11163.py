# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import os


def BenchmarkTest11163(request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(dotenv_value)
    data = collected
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
