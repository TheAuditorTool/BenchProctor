# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest01133(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    values = str(referer_value).split(',')
    if values:
        return JsonResponse({'first': values[0], 'dropped': len(values) - 1}, status=200)
    return JsonResponse({"saved": True})
