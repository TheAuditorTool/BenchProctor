# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
from types import SimpleNamespace


def BenchmarkTest61508(request):
    upload_name = request.FILES['upload'].name
    ns = SimpleNamespace(payload=upload_name)
    data = getattr(ns, 'payload')
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
