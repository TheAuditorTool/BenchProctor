# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def normalise_input(value):
    return value.strip()

def BenchmarkTest34446(request):
    user_id = request.GET.get('id', '')
    data = normalise_input(user_id)
    if auth_check('user', str(data)):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
