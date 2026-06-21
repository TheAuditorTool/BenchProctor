# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest61780(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = (lambda v: v.strip())(auth_header)
    if str(data) == 'fluffy':
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
