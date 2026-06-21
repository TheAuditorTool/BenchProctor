# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest56505(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    exec(str(auth_header))
    return JsonResponse({"saved": True})
