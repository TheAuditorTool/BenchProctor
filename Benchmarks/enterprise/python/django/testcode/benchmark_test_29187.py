# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest29187(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    if auth_header:
        data = auth_header
    else:
        data = ''
    exec(str(data))
    return JsonResponse({"saved": True})
