# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest70265(request):
    user_id = request.GET.get('id', '')
    data = str(user_id).replace('\x00', '')
    try:
        result = int(str(data))
    except ValueError as e:
        return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({"saved": True})
