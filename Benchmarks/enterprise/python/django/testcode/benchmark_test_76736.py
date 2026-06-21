# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest76736(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = '%s' % str(forwarded_ip)
    try:
        result = int(str(data))
    except ValueError as e:
        return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({"saved": True})
