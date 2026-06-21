# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest01140(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    if str(header_value).endswith(('/public', '/static', '/.')):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
