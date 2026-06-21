# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest56680(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = f'{auth_header:.200s}'
    if str(data) == 'fluffy':
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
