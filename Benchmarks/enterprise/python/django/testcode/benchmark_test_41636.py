# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
from dataclasses import dataclass
import os


@dataclass
class FormData:
    payload: str

def BenchmarkTest41636(request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    data = FormData(payload=dotenv_value).payload
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
