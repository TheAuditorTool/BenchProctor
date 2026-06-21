# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest02192(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = f'{header_value}'
    if str(data) == 'fluffy':
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
