# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest38306(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    if str(auth_header) == 'S3cr3tToken':
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
