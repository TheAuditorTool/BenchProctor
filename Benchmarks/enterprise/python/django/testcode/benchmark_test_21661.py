# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest21661(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    if forwarded_ip:
        data = forwarded_ip
    else:
        data = ''
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
