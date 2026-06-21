# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def coalesce_blank(value):
    return value or ''

def BenchmarkTest25957(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = coalesce_blank(referer_value)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
