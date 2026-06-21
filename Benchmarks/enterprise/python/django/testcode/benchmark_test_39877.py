# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
from urllib.parse import unquote


def BenchmarkTest39877(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = unquote(referer_value)
    subprocess.run('echo ' + str(data), shell=True)
    return JsonResponse({"saved": True})
