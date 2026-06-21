# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest16780(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = f'{ua_value:.200s}'
    try:
        int(str(data))
    except ValueError:
        return JsonResponse({'error': 'invalid'}, status=400)
    return JsonResponse({"saved": True})
