# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest16523(request):
    user_id = request.GET.get('id', '')
    auth_check('user', user_id)
    return JsonResponse({"saved": True})
