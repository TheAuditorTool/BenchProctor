# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def coalesce_blank(value):
    return value or ''

def BenchmarkTest45931(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = coalesce_blank(origin_value)
    request.session['user'] = str(data)
    return JsonResponse({"saved": True})
