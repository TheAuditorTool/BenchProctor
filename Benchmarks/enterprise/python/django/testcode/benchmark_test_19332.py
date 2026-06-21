# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def normalise_input(value):
    return value.strip()

def BenchmarkTest19332(request):
    upload_name = request.FILES['upload'].name
    data = normalise_input(upload_name)
    if auth_check('user', str(data)):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
