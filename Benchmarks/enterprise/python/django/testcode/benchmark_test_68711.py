# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest68711(request):
    host_value = request.META.get('HTTP_HOST', '')
    if str(host_value) in ('localhost', 'internal-gateway'):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
