# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest62314(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    int(str(auth_header))
    return JsonResponse({"saved": True})
