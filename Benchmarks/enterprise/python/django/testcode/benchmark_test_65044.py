# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import os
from types import SimpleNamespace


def BenchmarkTest65044(request):
    env_value = os.environ.get('USER_INPUT', '')
    ns = SimpleNamespace(payload=env_value)
    data = getattr(ns, 'payload')
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
