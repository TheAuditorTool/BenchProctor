# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest09731(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = default_blank(auth_header)
    if str(data) == 'S3cr3tToken':
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
