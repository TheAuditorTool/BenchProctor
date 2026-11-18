# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00265(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = ' '.join(str(multipart_value).split())
    try:
        _coerced = float(data)
    except (TypeError, ValueError):
        return JsonResponse({'error': 'invalid number'}, status=400)
    processed = _coerced
    exec(str(processed))
    return JsonResponse({"saved": True})
