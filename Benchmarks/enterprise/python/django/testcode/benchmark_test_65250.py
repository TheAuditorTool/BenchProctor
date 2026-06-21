# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest65250(request):
    raw_body = request.body.decode('utf-8')
    kind = 'json' if str(raw_body).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = raw_body
            data = parsed
        case _:
            data = raw_body
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
