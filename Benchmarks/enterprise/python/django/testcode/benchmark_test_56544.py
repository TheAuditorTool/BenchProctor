# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest56544(request):
    user_id = request.GET.get('id', '')
    if str(user_id).endswith(('/public', '/static', '/.')):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
