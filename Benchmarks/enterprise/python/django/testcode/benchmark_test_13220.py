# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest13220(request):
    user_id = request.GET.get('id', '')
    data = user_id if user_id else 'default'
    if str(data).endswith(('/public', '/static', '/.')):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
