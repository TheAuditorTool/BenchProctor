# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest21173(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    int(str(forwarded_ip))
    return JsonResponse({"saved": True})
