# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import re
from types import SimpleNamespace


def BenchmarkTest07445(request):
    user_id = request.GET.get('id', '')
    ns = SimpleNamespace(payload=user_id)
    data = getattr(ns, 'payload')
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(data).replace('\r', '').replace('\n', ''))
    logging.info('User action: ' + str(processed))
    return JsonResponse({"saved": True})
