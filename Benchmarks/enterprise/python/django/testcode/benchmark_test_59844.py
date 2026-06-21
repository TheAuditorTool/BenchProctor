# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess
from types import SimpleNamespace


def BenchmarkTest59844(request, path_param):
    path_value = path_param
    ns = SimpleNamespace(payload=path_value)
    data = getattr(ns, 'payload')
    subprocess.run(['echo', data], shell=False)
    return JsonResponse({"saved": True})
