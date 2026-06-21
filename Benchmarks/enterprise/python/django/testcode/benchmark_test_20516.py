# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest20516(request):
    user_id = request.GET.get('id', '')
    if not auth_check(request.session.get('user', ''), str(user_id)):
        return JsonResponse({'error': 'forbidden'}, status=403)
    return JsonResponse({"saved": True})
