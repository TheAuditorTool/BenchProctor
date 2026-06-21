# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


def BenchmarkTest35993(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    if re.search('[a-zA-Z0-9_-]+', str(auth_header)):
        return JsonResponse({'validated': str(auth_header)}, status=200)
    return JsonResponse({"saved": True})
