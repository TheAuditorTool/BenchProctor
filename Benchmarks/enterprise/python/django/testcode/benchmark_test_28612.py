# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import os


def BenchmarkTest28612(request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    parts = []
    for token in str(dotenv_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
