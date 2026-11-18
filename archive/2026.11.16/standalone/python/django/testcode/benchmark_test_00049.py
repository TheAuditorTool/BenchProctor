# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import unquote


def BenchmarkTest00049(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = unquote(referer_value)
    _coerced = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    processed = _coerced
    request.session['data'] = str(processed)
    return JsonResponse({"saved": True})
