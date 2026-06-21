# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest68884(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = '{}'.format(forwarded_ip)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return JsonResponse({"saved": True})
