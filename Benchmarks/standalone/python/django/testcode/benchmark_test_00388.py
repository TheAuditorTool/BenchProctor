# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00388(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = str(forwarded_ip).replace('\x00', '')
    _coerced = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    processed = _coerced
    exec(str(processed))
    return JsonResponse({"saved": True})
