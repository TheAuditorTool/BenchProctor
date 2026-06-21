# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest79196(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = f'{auth_header}'
    if str(data) == 'S3cr3tToken':
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
