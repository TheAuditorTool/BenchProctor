# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from app_runtime import auth_check


def BenchmarkTest35481(request):
    env_value = os.environ.get('USER_INPUT', '')
    if not auth_check(request.session.get('user', ''), str(env_value)):
        return JsonResponse({'error': 'forbidden'}, status=403)
    return JsonResponse({"saved": True})
