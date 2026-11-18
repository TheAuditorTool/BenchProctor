# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess


def BenchmarkTest00176(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = '%s' % str(ua_value)
    subprocess.run(['echo', data], shell=False)
    return JsonResponse({"saved": True})
