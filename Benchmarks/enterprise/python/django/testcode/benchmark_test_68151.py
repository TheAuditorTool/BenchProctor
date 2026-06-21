# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest68151(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = (lambda v: v.strip())(auth_header)
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return JsonResponse({"saved": True})
