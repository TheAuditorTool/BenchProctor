# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import re
from types import SimpleNamespace


def BenchmarkTest39285(request):
    xml_value = request.body.decode('utf-8')
    ns = SimpleNamespace(payload=xml_value)
    data = getattr(ns, 'payload')
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    os.chmod('/var/app/data/' + str(processed), 0o777)
    return JsonResponse({"saved": True})
