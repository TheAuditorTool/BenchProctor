# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest35591(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    values = str(header_value).split(',')
    if values:
        return JsonResponse({'first': values[0], 'dropped': len(values) - 1}, status=200)
    return JsonResponse({"saved": True})
