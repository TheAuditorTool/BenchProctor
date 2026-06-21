# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess
from urllib.parse import unquote


def BenchmarkTest55383(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = unquote(referer_value)
    subprocess.run(['echo', data], shell=False)
    return JsonResponse({"saved": True})
