# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest49917(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = forwarded_ip if forwarded_ip else 'default'
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
