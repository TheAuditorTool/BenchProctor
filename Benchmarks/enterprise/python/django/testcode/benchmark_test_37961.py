# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest37961(request):
    raw_body = request.body.decode('utf-8')
    data = ' '.join(str(raw_body).split())
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
