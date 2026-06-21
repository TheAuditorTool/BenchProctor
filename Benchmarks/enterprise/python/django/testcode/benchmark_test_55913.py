# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess
from types import SimpleNamespace


def BenchmarkTest55913(request):
    upload_name = request.FILES['upload'].name
    ns = SimpleNamespace(payload=upload_name)
    data = getattr(ns, 'payload')
    subprocess.run(['echo', data], shell=False)
    return JsonResponse({"saved": True})
