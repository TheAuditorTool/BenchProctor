# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest07073(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = f'{host_value:.200s}'
    if str(data) == 'fluffy':
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
