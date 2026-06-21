# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest60415(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = '{}'.format(host_value)
    values = str(data).split(',')
    if values:
        return JsonResponse({'first': values[0], 'dropped': len(values) - 1}, status=200)
    return JsonResponse({"saved": True})
