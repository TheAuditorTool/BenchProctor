# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from app_runtime import auth_check


def coalesce_blank(value):
    return value or ''

def BenchmarkTest58015(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = coalesce_blank(env_value)
    if not auth_check(request.session.get('user', ''), str(data)):
        return JsonResponse({'error': 'forbidden'}, status=403)
    return JsonResponse({"saved": True})
