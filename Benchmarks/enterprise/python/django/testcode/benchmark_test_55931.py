# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest55931(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data, _sep, _rest = str(ua_value).partition('\x00')
    try:
        os.setuid(int(str(data)) if str(data).isdigit() else 65534)
    except OSError:
        return JsonResponse({'error': 'privilege drop failed'}, status=500)
    return JsonResponse({"saved": True})
