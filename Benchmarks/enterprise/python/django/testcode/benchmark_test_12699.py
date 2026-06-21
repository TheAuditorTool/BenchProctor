# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest12699(request):
    user_id = request.GET.get('id', '')
    data = (lambda v: v.strip())(user_id)
    auth_check('user', data)
    return JsonResponse({"saved": True})
