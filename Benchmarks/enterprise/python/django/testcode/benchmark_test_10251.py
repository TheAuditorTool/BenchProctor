# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest10251(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data, _sep, _rest = str(forwarded_ip).partition('\x00')
    eval(str(data))
    return JsonResponse({"saved": True})
