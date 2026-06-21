# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest51375(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = '{}'.format(forwarded_ip)
    request.session['user'] = str(data)
    return JsonResponse({"saved": True})
