# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest43144(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    if str(forwarded_ip) == 'S3cr3tToken':
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
