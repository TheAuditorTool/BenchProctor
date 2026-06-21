# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest36133(request):
    upload_name = request.FILES['upload'].name
    if not auth_check(request.session.get('user', ''), str(upload_name)):
        return JsonResponse({'error': 'forbidden'}, status=403)
    return JsonResponse({"saved": True})
