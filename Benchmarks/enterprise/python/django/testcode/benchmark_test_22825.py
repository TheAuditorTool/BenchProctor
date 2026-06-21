# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest22825(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = forwarded_ip if forwarded_ip else 'default'
    int(str(data))
    return JsonResponse({"saved": True})
