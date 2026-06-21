# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest34839(request):
    raw_body = request.body.decode('utf-8')
    data = f'{raw_body:.200s}'
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return JsonResponse({"saved": True})
