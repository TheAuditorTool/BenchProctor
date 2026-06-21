# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest27420(request):
    raw_body = request.body.decode('utf-8')
    kind = 'json' if str(raw_body).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = raw_body
            data = parsed
        case _:
            data = raw_body
    eval(str(data))
    return JsonResponse({"saved": True})
