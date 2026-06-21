# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest34891(request):
    raw_body = request.body.decode('utf-8')
    data = f'{raw_body}'
    int(str(data))
    return JsonResponse({"saved": True})
