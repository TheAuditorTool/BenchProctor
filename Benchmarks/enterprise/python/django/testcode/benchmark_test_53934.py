# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest53934(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data, _sep, _rest = str(referer_value).partition('\x00')
    try:
        result = int(str(data))
    except ValueError as e:
        return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({"saved": True})
