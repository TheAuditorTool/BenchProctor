# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest79825(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = '{}'.format(host_value)
    try:
        int(str(data))
    except ValueError:
        return JsonResponse({'error': 'invalid'}, status=400)
    return JsonResponse({"saved": True})
