# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest12010(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    if not str(forwarded_ip).isdigit():
        raise ValueError('invalid input: ' + str(forwarded_ip))
    return JsonResponse({"saved": True})
