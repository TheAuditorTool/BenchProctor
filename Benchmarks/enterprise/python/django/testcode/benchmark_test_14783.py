# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest14783(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    prefix = ''
    data = prefix + str(origin_value)
    values = str(data).split(',')
    if values:
        return JsonResponse({'first': values[0], 'dropped': len(values) - 1}, status=200)
    return JsonResponse({"saved": True})
