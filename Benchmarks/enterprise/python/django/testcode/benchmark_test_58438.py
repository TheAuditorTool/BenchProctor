# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest58438(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    try:
        int(str(forwarded_ip))
    except ValueError:
        return JsonResponse({'error': 'invalid'}, status=400)
    return JsonResponse({"saved": True})
