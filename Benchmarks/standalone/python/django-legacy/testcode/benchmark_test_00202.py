# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00202(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    request.session.update({'data': str(ua_value)})
    return JsonResponse({"saved": True})
