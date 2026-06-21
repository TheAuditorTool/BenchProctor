# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest20440(request):
    upload_name = request.FILES['upload'].name
    data = str(upload_name).replace('\x00', '')
    auth_check('user', data)
    return JsonResponse({"saved": True})
