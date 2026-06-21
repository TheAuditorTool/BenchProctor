# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest08483(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    prefix = ''
    data = prefix + str(auth_header)
    eval(str(data))
    return JsonResponse({"saved": True})
