# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00539(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = '%s' % (header_value,)
    _coerced = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    processed = _coerced
    request.session['data'] = str(processed)
    return JsonResponse({"saved": True})
