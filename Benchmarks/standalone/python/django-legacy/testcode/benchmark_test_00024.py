# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00024(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    def normalize(value):
        return value.strip()
    data = normalize(referer_value)
    try:
        _coerced = float(data)
    except (TypeError, ValueError):
        return JsonResponse({'error': 'invalid number'}, status=400)
    processed = _coerced
    code = compile(str(processed), '<rule>', 'exec')
    exec(code)
    return JsonResponse({"saved": True})
