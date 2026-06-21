# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from app_runtime import auth_check


def BenchmarkTest11182(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value:.200s}'
    if not auth_check(str(data), request.session.get('token')):
        return JsonResponse({'error': 'unauthorized'}, status=401)
    return JsonResponse({"saved": True})
