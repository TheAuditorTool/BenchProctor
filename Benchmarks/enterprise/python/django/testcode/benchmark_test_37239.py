# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest37239(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    prefix = ''
    data = prefix + str(auth_header)
    if str(data) == 'fluffy':
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
