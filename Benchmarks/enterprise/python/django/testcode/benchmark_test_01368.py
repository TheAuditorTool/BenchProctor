# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest01368(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = str(host_value).replace('\x00', '')
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
