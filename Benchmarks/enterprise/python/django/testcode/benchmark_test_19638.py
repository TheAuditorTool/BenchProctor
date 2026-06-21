# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest19638(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = '{}'.format(host_value)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
