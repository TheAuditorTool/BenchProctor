# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
from dataclasses import dataclass
import os


@dataclass
class FormData:
    payload: str

def BenchmarkTest03512(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = FormData(payload=env_value).payload
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
