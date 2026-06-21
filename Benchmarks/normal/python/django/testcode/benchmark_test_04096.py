# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest04096(request):
    raw_body = request.body.decode('utf-8')
    data, _sep, _rest = str(raw_body).partition('\x00')
    exec(str(data))
    return JsonResponse({"saved": True})
