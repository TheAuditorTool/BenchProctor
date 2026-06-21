# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest17302(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    try:
        result = int(str(auth_header))
    except ValueError as e:
        return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({"saved": True})
