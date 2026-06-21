# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import os
from types import SimpleNamespace


def BenchmarkTest44623(request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    ns = SimpleNamespace(payload=dotenv_value)
    data = getattr(ns, 'payload')
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
