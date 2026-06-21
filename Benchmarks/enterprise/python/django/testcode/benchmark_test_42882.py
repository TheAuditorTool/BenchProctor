# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest42882(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = referer_value if referer_value else 'default'
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    request.session['data'] = str(processed)
    return JsonResponse({"saved": True})
