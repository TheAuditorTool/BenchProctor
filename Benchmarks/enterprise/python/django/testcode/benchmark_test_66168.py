# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest66168(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    if str(auth_header) == 'is_admin':
        return JsonResponse({'access': 'granted', 'role': 'admin'}, status=200)
    return JsonResponse({"saved": True})
