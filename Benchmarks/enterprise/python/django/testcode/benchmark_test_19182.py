# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest19182(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = (lambda v: v.strip())(forwarded_ip)
    request.session['user'] = str(data)
    return JsonResponse({"saved": True})
