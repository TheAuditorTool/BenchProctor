# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest42425(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = f'{forwarded_ip:.200s}'
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
