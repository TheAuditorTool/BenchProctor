# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest26269(request):
    user_id = request.GET.get('id', '')
    data = user_id if user_id else 'default'
    try:
        result = int(str(data))
    except ValueError as e:
        return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({"saved": True})
