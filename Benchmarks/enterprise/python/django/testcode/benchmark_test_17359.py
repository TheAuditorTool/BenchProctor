# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest17359(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = (lambda v: v.strip())(origin_value)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
