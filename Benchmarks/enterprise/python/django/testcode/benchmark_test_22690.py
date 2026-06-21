# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest22690(request):
    upload_name = request.FILES['upload'].name
    if auth_check('user', str(upload_name)):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
