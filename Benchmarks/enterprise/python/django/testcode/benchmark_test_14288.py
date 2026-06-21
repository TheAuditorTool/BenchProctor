# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import re
import os


def BenchmarkTest14288(request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    data = f'{dotenv_value:.200s}'
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(data).replace('\r', '').replace('\n', ''))
    logging.info('User action: ' + str(processed))
    return JsonResponse({"saved": True})
