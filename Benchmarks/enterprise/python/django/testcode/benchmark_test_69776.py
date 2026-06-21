# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest69776(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = auth_header if auth_header else 'default'
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return JsonResponse({"saved": True})
