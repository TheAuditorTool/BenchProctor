# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import os


def BenchmarkTest70109(request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    logging.info('User action: ' + str(dotenv_value))
    return JsonResponse({"saved": True})
