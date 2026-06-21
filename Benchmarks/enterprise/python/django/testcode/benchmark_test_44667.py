# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest44667(request):
    raw_body = request.body.decode('utf-8')
    data = raw_body if raw_body else 'default'
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return JsonResponse({"saved": True})
