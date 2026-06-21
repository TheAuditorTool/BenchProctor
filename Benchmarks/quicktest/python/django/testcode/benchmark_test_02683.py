# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest02683(request):
    upload_name = request.FILES['upload'].name
    data = (lambda v: v.strip())(upload_name)
    auth_check('user', data)
    return JsonResponse({"saved": True})
