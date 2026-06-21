# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest37792(request):
    raw_body = request.body.decode('utf-8')
    data = f'{raw_body:.200s}'
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
