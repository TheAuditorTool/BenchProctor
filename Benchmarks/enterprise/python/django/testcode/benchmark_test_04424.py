# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest04424(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = '%s' % str(host_value)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
