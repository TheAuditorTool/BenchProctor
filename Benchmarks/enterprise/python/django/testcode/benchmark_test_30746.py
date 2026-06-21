# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest30746(request):
    upload_name = request.FILES['upload'].name
    auth_check('user', upload_name)
    return JsonResponse({"saved": True})
