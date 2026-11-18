# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00631(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    parts = str(ua_value).split(',')
    data = ' '.join(parts)
    _coerced = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    processed = _coerced
    exec(str(processed))
    return JsonResponse({"saved": True})
