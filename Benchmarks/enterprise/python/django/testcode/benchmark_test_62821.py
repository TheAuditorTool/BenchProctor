# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest62821(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    if auth_header:
        data = auth_header
    else:
        data = ''
    result = 100 / int(str(data))
    return JsonResponse({"saved": True})
