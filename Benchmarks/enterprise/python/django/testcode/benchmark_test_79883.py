# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest79883(request):
    user_id = request.GET.get('id', '')
    data = user_id if user_id else 'default'
    divisor = int(str(data)) if str(data).isdigit() else 1
    if divisor == 0:
        return JsonResponse({'error': 'zero division'}, status=400)
    result = 100 / divisor
    return JsonResponse({"saved": True})
