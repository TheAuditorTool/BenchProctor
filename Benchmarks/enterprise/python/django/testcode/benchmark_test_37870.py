# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import json
import os


def BenchmarkTest37870(request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    try:
        data = json.loads(dotenv_value).get('value', dotenv_value)
    except (json.JSONDecodeError, AttributeError):
        data = dotenv_value
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
