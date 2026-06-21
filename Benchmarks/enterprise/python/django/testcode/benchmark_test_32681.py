# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest32681(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = referer_value if referer_value else 'default'
    try:
        int(str(data))
    except ValueError:
        return JsonResponse({'error': 'invalid'}, status=400)
    return JsonResponse({"saved": True})
