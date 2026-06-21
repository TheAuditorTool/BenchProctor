# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest14659(request):
    upload_name = request.FILES['upload'].name
    data = f'{upload_name:.200s}'
    auth_check('user', data)
    return JsonResponse({"saved": True})
