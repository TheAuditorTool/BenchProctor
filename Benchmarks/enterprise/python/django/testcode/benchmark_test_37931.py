# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest37931(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    def normalize(value):
        return value.strip()
    data = normalize(forwarded_ip)
    int(str(data))
    return JsonResponse({"saved": True})
