# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest01098(request):
    user_id = request.GET.get('id', '')
    data = f'{user_id:.200s}'
    if str(data).endswith(('/public', '/static', '/.')):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
