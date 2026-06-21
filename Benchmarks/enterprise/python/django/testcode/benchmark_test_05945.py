# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import re
import os


def BenchmarkTest05945(request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    def normalize(value):
        return value.strip()
    data = normalize(dotenv_value)
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(data).replace('\r', '').replace('\n', ''))
    logging.info('User action: ' + str(processed))
    return JsonResponse({"saved": True})
