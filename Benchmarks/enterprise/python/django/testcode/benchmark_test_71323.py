# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest71323(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    parts = str(referer_value).split(',')
    data = ','.join(parts)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
