# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest63092(request):
    user_id = request.GET.get('id', '')
    data = ' '.join(str(user_id).split())
    auth_check('user', data)
    return JsonResponse({"saved": True})
