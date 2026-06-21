# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest59646(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = referer_value if referer_value else 'default'
    request.session['user'] = str(data)
    return JsonResponse({"saved": True})
