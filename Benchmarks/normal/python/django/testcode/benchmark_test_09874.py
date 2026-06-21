# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest09874(request):
    raw_body = request.body.decode('utf-8')
    kind = 'json' if str(raw_body).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = raw_body
            data = parsed
        case _:
            data = raw_body
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
