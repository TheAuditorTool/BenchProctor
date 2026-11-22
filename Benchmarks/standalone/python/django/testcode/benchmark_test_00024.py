# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00024(request):
    raw_body = request.body.decode('utf-8')
    if raw_body:
        data = raw_body
    else:
        data = ''
    try:
        _coerced = float(data)
    except (TypeError, ValueError):
        return JsonResponse({'error': 'invalid number'}, status=400)
    processed = _coerced
    code = compile(str(processed), '<rule>', 'exec')
    exec(code)
    return JsonResponse({"saved": True})
