# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest09669(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = f'{referer_value:.200s}'
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
