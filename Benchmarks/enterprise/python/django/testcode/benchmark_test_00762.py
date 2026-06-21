# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest00762(request):
    upload_name = request.FILES['upload'].name
    data = ' '.join(str(upload_name).split())
    auth_check('user', data)
    return JsonResponse({"saved": True})
