# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest09341(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = '%s' % (ua_value,)
    request.session['user'] = str(data)
    return JsonResponse({"saved": True})
