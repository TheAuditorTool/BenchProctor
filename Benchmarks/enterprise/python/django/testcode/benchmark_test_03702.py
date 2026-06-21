# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest03702(request):
    host_value = request.META.get('HTTP_HOST', '')
    prefix = ''
    data = prefix + str(host_value)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
