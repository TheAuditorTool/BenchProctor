# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest03720(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = str(host_value).replace('\x00', '')
    if str(data) == 'fluffy':
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
