# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest59685(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    prefix = ''
    data = prefix + str(forwarded_ip)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
