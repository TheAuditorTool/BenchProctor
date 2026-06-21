# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest77384(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    request.session['data'] = str(referer_value)
    return JsonResponse({"saved": True})
