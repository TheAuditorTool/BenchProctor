# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest27373(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = str(host_value).replace('\x00', '')
    values = str(data).split(',')
    if values:
        return JsonResponse({'first': values[0], 'dropped': len(values) - 1}, status=200)
    return JsonResponse({"saved": True})
