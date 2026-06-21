# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from urllib.parse import unquote


def BenchmarkTest55385(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = unquote(referer_value)
    try:
        os.setuid(int(str(data)) if str(data).isdigit() else 65534)
    except OSError:
        return JsonResponse({'error': 'privilege drop failed'}, status=500)
    return JsonResponse({"saved": True})
