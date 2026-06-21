# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest07099(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = str(forwarded_ip).replace('\x00', '')
    result = 100 / int(str(data))
    return JsonResponse({"saved": True})
