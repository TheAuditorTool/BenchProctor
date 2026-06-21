# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def relay_value(value):
    return value

def BenchmarkTest78652(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = relay_value(forwarded_ip)
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return JsonResponse({"saved": True})
