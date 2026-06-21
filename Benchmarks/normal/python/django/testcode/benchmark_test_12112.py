# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest12112(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    if not auth_check(request.session.get('user', ''), str(referer_value)):
        return JsonResponse({'error': 'forbidden'}, status=403)
    return JsonResponse({"saved": True})
