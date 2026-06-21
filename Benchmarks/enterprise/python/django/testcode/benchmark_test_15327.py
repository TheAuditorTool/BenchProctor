# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest15327(request):
    raw_body = request.body.decode('utf-8')
    data = f'{raw_body:.200s}'
    int(str(data))
    return JsonResponse({"saved": True})
