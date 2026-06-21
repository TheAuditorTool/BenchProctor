# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest21099(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = '{}'.format(forwarded_ip)
    result = 100 / int(str(data))
    return JsonResponse({"saved": True})
