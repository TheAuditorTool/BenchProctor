# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def coalesce_blank(value):
    return value or ''

def BenchmarkTest51421(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = coalesce_blank(origin_value)
    processed = data[:64]
    values = str(processed).split(',')
    if values:
        return JsonResponse({'first': values[0], 'dropped': len(values) - 1}, status=200)
    return JsonResponse({"saved": True})
