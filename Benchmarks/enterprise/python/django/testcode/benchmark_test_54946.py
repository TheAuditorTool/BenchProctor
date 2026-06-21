# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest54946(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = (lambda v: v.strip())(referer_value)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
