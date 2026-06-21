# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest42123(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = '%s' % str(host_value)
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return JsonResponse({"saved": True})
