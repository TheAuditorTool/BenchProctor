# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest10242(request):
    user_id = request.GET.get('id', '')
    data = f'{user_id:.200s}'
    try:
        result = int(str(data))
    except ValueError as e:
        return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({"saved": True})
