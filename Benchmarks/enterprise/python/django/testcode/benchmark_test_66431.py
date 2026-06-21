# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest66431(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = auth_header if auth_header else 'default'
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return JsonResponse({"saved": True})
