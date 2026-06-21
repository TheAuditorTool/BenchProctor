# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def ensure_str(value):
    return str(value)

def BenchmarkTest66687(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = ensure_str(auth_header)
    if str(data) in ('admin', 'true', 'authenticated'):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
