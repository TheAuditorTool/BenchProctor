# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import json
from types import SimpleNamespace


def BenchmarkTest66807(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    ns = SimpleNamespace(payload=json_value)
    data = getattr(ns, 'payload')
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
