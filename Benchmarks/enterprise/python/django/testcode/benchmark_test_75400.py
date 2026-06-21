# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest75400(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = ' '.join(str(ua_value).split())
    try:
        os.setuid(int(str(data)) if str(data).isdigit() else 65534)
    except OSError:
        pass
    return JsonResponse({"saved": True})
