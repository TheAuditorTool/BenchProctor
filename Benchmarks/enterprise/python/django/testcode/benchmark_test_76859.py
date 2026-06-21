# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest76859(request):
    user_id = request.GET.get('id', '')
    parts = str(user_id).split(',')
    data = ','.join(parts)
    auth_check('user', data)
    return JsonResponse({"saved": True})
