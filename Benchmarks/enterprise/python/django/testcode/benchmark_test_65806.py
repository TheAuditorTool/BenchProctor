# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest65806(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    if str(origin_value) in ('admin', 'true', 'authenticated'):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
