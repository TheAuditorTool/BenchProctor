# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00152(request):
    user_id = request.GET.get('id', '')
    data = (lambda v: v.strip())(user_id)
    try:
        _coerced = float(data)
    except (TypeError, ValueError):
        return JsonResponse({'error': 'invalid number'}, status=400)
    processed = _coerced
    eval(str(processed))
    return JsonResponse({"saved": True})
