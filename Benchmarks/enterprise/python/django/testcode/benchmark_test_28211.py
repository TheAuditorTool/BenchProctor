# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest28211(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = '%s' % (host_value,)
    try:
        int(str(data))
    except ValueError:
        return JsonResponse({'error': 'invalid'}, status=400)
    return JsonResponse({"saved": True})
