# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest38037(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    if auth_header:
        data = auth_header
    else:
        data = ''
    int(str(data))
    return JsonResponse({"saved": True})
