# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest18612(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = str(forwarded_ip).replace('\x00', '')
    int(str(data))
    return JsonResponse({"saved": True})
