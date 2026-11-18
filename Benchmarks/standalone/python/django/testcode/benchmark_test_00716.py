# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00716(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    def normalize(value):
        return value.strip()
    data = normalize(auth_header)
    _coerced = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    processed = _coerced
    request.session['data'] = str(processed)
    return JsonResponse({"saved": True})
