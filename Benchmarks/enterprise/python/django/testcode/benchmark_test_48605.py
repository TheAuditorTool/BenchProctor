# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest48605(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = '%s' % (host_value,)
    request.session.set_expiry(1800)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
