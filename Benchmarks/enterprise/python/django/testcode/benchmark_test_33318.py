# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest33318(request):
    raw_body = request.body.decode('utf-8')
    data, _sep, _rest = str(raw_body).partition('\x00')
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
