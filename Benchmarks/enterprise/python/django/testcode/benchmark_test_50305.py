# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest50305(request):
    user_id = request.GET.get('id', '')
    def normalize(value):
        return value.strip()
    data = normalize(user_id)
    if not auth_check(str(data), request.session.get('token')):
        return JsonResponse({'error': 'unauthorized'}, status=401)
    return JsonResponse({"saved": True})
