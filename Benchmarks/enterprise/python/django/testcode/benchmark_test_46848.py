# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest46848(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = (lambda v: v.strip())(auth_header)
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return JsonResponse({"saved": True})
