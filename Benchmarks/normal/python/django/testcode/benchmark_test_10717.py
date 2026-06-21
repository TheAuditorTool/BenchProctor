# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest10717(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    try:
        os.setuid(int(str(referer_value)) if str(referer_value).isdigit() else 65534)
    except OSError:
        return JsonResponse({'error': 'privilege drop failed'}, status=500)
    return JsonResponse({"saved": True})
