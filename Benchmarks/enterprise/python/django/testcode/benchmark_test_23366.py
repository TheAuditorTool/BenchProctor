# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest23366(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data, _sep, _rest = str(auth_header).partition('\x00')
    result = 100 / int(str(data))
    return JsonResponse({"saved": True})
