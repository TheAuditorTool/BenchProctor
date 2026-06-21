# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest08204(request):
    host_value = request.META.get('HTTP_HOST', '')
    parts = str(host_value).split(',')
    data = ','.join(parts)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
