# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00098(request, path_param):
    path_value = path_param
    parts = str(path_value).split(',')
    data = ' '.join(parts)
    _coerced = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    processed = _coerced
    request.session['data'] = str(processed)
    return JsonResponse({"saved": True})
