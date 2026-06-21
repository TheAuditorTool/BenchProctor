# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest20079(request):
    user_id = request.GET.get('id', '')
    prefix = ''
    data = prefix + str(user_id)
    try:
        result = int(str(data))
    except ValueError as e:
        return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({"saved": True})
