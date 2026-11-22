# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00081(request):
    multipart_value = request.POST.get('multipart_field', '')
    parts = str(multipart_value).split(',')
    data = ' '.join(parts)
    try:
        _coerced = float(data)
    except (TypeError, ValueError):
        return JsonResponse({'error': 'invalid number'}, status=400)
    processed = _coerced
    eval(str(processed))
    return JsonResponse({"saved": True})
