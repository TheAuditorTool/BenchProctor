# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from urllib.parse import unquote
import subprocess


def BenchmarkTest02458(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = unquote(referer_value)
    subprocess.run([str(data), '--status'], shell=False)
    return JsonResponse({"saved": True})
