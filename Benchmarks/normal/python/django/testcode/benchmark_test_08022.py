# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import re
from types import SimpleNamespace
import subprocess


def BenchmarkTest08022(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    ns = SimpleNamespace(payload=ua_value)
    data = getattr(ns, 'payload')
    if not re.fullmatch('^[\\w\\s.;|&$`\'\\"_/\\-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    subprocess.run([str(processed), '--status'], shell=False)
    return JsonResponse({"saved": True})
