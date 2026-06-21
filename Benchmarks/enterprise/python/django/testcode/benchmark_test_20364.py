# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest20364(request):
    host_value = request.META.get('HTTP_HOST', '')
    if host_value:
        data = host_value
    else:
        data = ''
    request.session['user'] = str(data)
    return JsonResponse({"saved": True})
