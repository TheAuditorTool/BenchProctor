# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest39531(request):
    upload_name = request.FILES['upload'].name
    data = upload_name if upload_name else 'default'
    auth_check('user', data)
    return JsonResponse({"saved": True})
