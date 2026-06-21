# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest32761(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    prefix = ''
    data = prefix + str(origin_value)
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return JsonResponse({"saved": True})
