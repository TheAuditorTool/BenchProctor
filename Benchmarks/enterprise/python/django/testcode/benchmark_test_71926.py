# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest71926(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = str(ua_value).replace('\x00', '')
    request.session['user'] = str(data)
    return JsonResponse({"saved": True})
