# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest25355(request):
    user_id = request.GET.get('id', '')
    data = f'{user_id:.200s}'
    auth_check('user', data)
    return JsonResponse({"saved": True})
