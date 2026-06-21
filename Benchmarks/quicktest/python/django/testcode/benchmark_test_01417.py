# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest01417(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = f'{host_value:.200s}'
    exec(str(data))
    return JsonResponse({"saved": True})
