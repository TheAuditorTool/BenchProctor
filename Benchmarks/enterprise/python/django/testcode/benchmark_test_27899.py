# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest27899(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    try:
        os.setuid(int(str(ua_value)) if str(ua_value).isdigit() else 65534)
    except OSError:
        pass
    return JsonResponse({"saved": True})
