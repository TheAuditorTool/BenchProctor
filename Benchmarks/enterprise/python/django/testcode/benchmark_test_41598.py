# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest41598(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    eval(str(forwarded_ip))
    return JsonResponse({"saved": True})
