# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00620(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = str(forwarded_ip).replace('\x00', '')
    try:
        _coerced = float(data)
    except (TypeError, ValueError):
        return JsonResponse({'error': 'invalid number'}, status=400)
    processed = _coerced
    request.session['data'] = str(processed)
    return JsonResponse({"saved": True})
