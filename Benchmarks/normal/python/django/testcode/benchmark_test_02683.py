# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest02683(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = f'{referer_value}'
    request.session['user'] = str(data)
    return JsonResponse({"saved": True})
