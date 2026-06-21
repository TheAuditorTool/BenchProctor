# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest46327(request):
    user_id = request.GET.get('id', '')
    data = user_id if user_id else 'default'
    try:
        int(str(data))
    except ValueError:
        return JsonResponse({'error': 'invalid'}, status=400)
    return JsonResponse({"saved": True})
