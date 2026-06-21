# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest38496(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = f'{host_value:.200s}'
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return JsonResponse({"saved": True})
