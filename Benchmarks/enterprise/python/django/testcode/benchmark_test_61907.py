# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest61907(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    processed = 'true' if str(header_value).lower() in ('true', '1', 'yes', 'on') else 'false'
    request.session['data'] = str(processed)
    return JsonResponse({"saved": True})
