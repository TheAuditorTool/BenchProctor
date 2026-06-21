# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest24783(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = '{}'.format(auth_header)
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return JsonResponse({"saved": True})
