# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest72703(request):
    raw_body = request.body.decode('utf-8')
    if raw_body:
        data = raw_body
    else:
        data = ''
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return JsonResponse({"saved": True})
