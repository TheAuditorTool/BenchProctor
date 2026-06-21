# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess
from types import SimpleNamespace


def BenchmarkTest43907(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    ns = SimpleNamespace(payload=auth_header)
    data = getattr(ns, 'payload')
    subprocess.run(['echo', data], shell=False)
    return JsonResponse({"saved": True})
