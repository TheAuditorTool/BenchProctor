# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest08407(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    try:
        os.setuid(int(str(auth_header)) if str(auth_header).isdigit() else 65534)
    except OSError:
        return JsonResponse({'error': 'privilege drop failed'}, status=500)
    return JsonResponse({"saved": True})
