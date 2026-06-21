# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest80332(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = '{}'.format(auth_header)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return JsonResponse({"saved": True})
