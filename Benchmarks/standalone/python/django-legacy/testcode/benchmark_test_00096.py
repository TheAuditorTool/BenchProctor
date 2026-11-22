# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00096(request):
    upload_name = request.FILES['upload'].name
    if upload_name:
        data = upload_name
    else:
        data = ''
    _coerced = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    processed = _coerced
    request.session['data'] = str(processed)
    return JsonResponse({"saved": True})
