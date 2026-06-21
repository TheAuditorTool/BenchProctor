# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest18618(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    parts = str(auth_header).split(',')
    data = ','.join(parts)
    try:
        int(str(data))
    except ValueError:
        return JsonResponse({'error': 'invalid'}, status=400)
    return JsonResponse({"saved": True})
