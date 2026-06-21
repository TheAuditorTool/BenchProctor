# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest22055(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = '%s' % (ua_value,)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
