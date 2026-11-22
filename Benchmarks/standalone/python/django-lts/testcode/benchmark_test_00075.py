# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00075(request):
    field_value = request.POST.get('field', '')
    data = field_value if field_value else 'default'
    try:
        _coerced = float(data)
    except (TypeError, ValueError):
        return JsonResponse({'error': 'invalid number'}, status=400)
    processed = _coerced
    exec(str(processed))
    return JsonResponse({"saved": True})
